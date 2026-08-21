"""
Sintonización de controladores PID con error compuesto y búsqueda en árbol binario
====================================================================================

Proyecto: FuzzyFrog.AI — ai-lab/proyectos/industria
Autor base del prototipo: Héctor (notebook original) · Limpieza y documentación: Alan López

Qué hace este script
---------------------
1. Modela una planta G(s) y un controlador PID en la representación clásica de
   funciones de transferencia (numpy.polymul / numpy.polyadd), igual que en el
   notebook original.
2. Genera una malla logarítmica de combinaciones (Kp, Ki, Kd).
3. Simula cada combinación en lazo cerrado con scipy.signal.lsim.
4. Evalúa un ERROR COMPUESTO por candidato, combinando:
      - IAE            (integral del error absoluto)
      - Overshoot (%)
      - Tiempo de subida
      - Energía de la señal de control  (∫|u| dt)
      - Error en estado estacionario
      - Penalización de oscilaciones (cruces con la referencia)
5. Inserta cada candidato en un árbol binario ordenado por error compuesto,
   de forma que el recorrido inorden entrega siempre el ranking completo y
   la estructura queda lista para una búsqueda incremental (por ejemplo,
   agregar generaciones de un algoritmo genético sin reprocesar todo).
6. Valida el Top-3 con una referencia distinta a la usada para sintonizar
   (entrada escalón), para evitar sobreajustar la señal de búsqueda.

Por qué esto y no solo MSE
---------------------------
El MSE por sí solo premia ganancias que reducen el error promedio aunque el
sistema oscile o gaste energía de control innecesaria. El hallazgo central
de este caso de estudio es que la función objetivo importa más que el
algoritmo de búsqueda: aquí se usa una malla logarítmica simple, pero el
mismo error compuesto es el que se usaría con un Algoritmo Genético o
Evolución Diferencial (ver referencias en el README).

Requisitos: numpy, scipy, matplotlib (ver requirements.txt)
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid as cumtrapz
from scipy.signal import TransferFunction, lsim


# ──────────────────────────────────────────────────────────────────────────
# 1. Álgebra de funciones de transferencia
# ──────────────────────────────────────────────────────────────────────────

def crear_pid(Kp: float, Ki: float, Kd: float) -> TransferFunction:
    """PID en forma de función de transferencia: (Kd*s^2 + Kp*s + Ki) / s"""
    num = [Kd, Kp, Ki]
    den = [1, 0]
    return TransferFunction(num, den)


def series_tf(G1: TransferFunction, G2: TransferFunction) -> TransferFunction:
    """Conexión en serie (cascada) de dos funciones de transferencia."""
    num = np.polymul(G1.num, G2.num)
    den = np.polymul(G1.den, G2.den)
    return TransferFunction(num, den)


def feedback(G: TransferFunction) -> TransferFunction:
    """Realimentación unitaria negativa: T(s) = G(s) / (1 + G(s))."""
    num = np.polymul(G.num, [1])
    den = np.polyadd(np.polymul(G.num, [1]), np.polymul(G.den, [1]))
    return TransferFunction(num, den)


# ──────────────────────────────────────────────────────────────────────────
# 2. Nodo de árbol binario ordenado por error compuesto
# ──────────────────────────────────────────────────────────────────────────

class NodoPID:
    """Candidato de sintonización PID con sus métricas de desempeño."""

    __slots__ = (
        "Kp", "Ki", "Kd", "error_compuesto", "iae", "os", "tr",
        "energia", "ess", "left", "right",
    )

    def __init__(self, Kp, Ki, Kd, error_compuesto, iae, os_, tr, energia, ess):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.error_compuesto = error_compuesto
        self.iae = iae
        self.os = os_
        self.tr = tr
        self.energia = energia
        self.ess = ess
        self.left = None
        self.right = None


def insertar_nodo(raiz: NodoPID | None, nodo: NodoPID) -> NodoPID:
    """Inserta un candidato en el árbol, ordenado por error_compuesto."""
    if raiz is None:
        return nodo
    if nodo.error_compuesto < raiz.error_compuesto:
        raiz.left = insertar_nodo(raiz.left, nodo)
    else:
        raiz.right = insertar_nodo(raiz.right, nodo)
    return raiz


def recorrido_inorden(nodo: NodoPID | None, lista=None) -> list[NodoPID]:
    """Recorrido inorden: entrega la lista ordenada de menor a mayor error."""
    if lista is None:
        lista = []
    if nodo is not None:
        recorrido_inorden(nodo.left, lista)
        lista.append(nodo)
        recorrido_inorden(nodo.right, lista)
    return lista


# ──────────────────────────────────────────────────────────────────────────
# 3. Simulación y error compuesto
# ──────────────────────────────────────────────────────────────────────────

def simular_lazo_cerrado(Kp, Ki, Kd, t, ref, G):
    """
    Simula el lazo cerrado PID + planta y devuelve el error compuesto y
    sus componentes individuales. Si el sistema es inestable o la
    simulación falla, devuelve infinito para descartar el candidato.
    """
    C = crear_pid(Kp, Ki, Kd)
    T = feedback(series_tf(C, G))

    try:
        _, y, _ = lsim(T, U=ref, T=t)
    except Exception:
        return dict(error_compuesto=np.inf, iae=np.inf, os=np.inf,
                    tr=np.inf, energia=np.inf, ess=np.inf)

    e = ref - y
    iae = np.trapezoid(np.abs(e), t)
    steady_state_error = np.mean(np.abs(e[int(len(e) * 0.9):]))

    # Señal de control u(t) = Kp*e + Ki*∫e dt + Kd*de/dt
    dt = t[1] - t[0]
    ei = cumtrapz(e, t, initial=0)
    ed = np.gradient(e, dt)
    u = Kp * e + Ki * ei + Kd * ed
    energia_control = np.trapezoid(np.abs(u), t)

    # Overshoot relativo al valor final de referencia
    y_max = np.max(y)
    ref_max = np.max(ref)
    overshoot = ((y_max - ref_max) / ref_max) * 100 if ref_max != 0 else 0.0

    # Tiempo de subida (90% del valor final)
    idx_tr = np.where(y >= 0.9 * ref_max)[0]
    tr = t[idx_tr[0]] if idx_tr.size > 0 else t[-1]

    # Penalización por oscilaciones: cruces de la salida con la referencia
    n_cruces = np.count_nonzero(np.diff(np.sign(ref - y)))
    penalizacion_oscilacion = n_cruces / len(t)

    # Normalizadores (mismo orden de magnitud entre componentes)
    max_tr = t[-1]
    max_os = 100.0
    max_energia = 10.0

    error_compuesto = (
        0.30 * iae
        + 0.20 * (abs(overshoot) / max_os)
        + 0.15 * (tr / max_tr)
        + 0.15 * (energia_control / max_energia)
        + 0.10 * steady_state_error
        + 0.10 * penalizacion_oscilacion
    )

    return dict(error_compuesto=error_compuesto, iae=iae, os=overshoot,
                tr=tr, energia=energia_control, ess=steady_state_error)


def simular_salida(Kp, Ki, Kd, t, ref, G):
    """Devuelve solo la salida y(t), para graficar la respuesta final."""
    C = crear_pid(Kp, Ki, Kd)
    T = feedback(series_tf(C, G))
    _, y, _ = lsim(T, U=ref, T=t)
    return y


# ──────────────────────────────────────────────────────────────────────────
# 4. Búsqueda en malla logarítmica
# ──────────────────────────────────────────────────────────────────────────

def buscar_pid(
    G: TransferFunction,
    kp_range=(0.1, 15.0),
    ki_range=(0.001, 3.0),
    kd_range=(0.01, 3.0),
    n_por_eje: int = 10,
    t_final: float = 15.0,
    n_puntos: int = 1500,
    top_n: int = 3,
    verbose: bool = True,
):
    """
    Busca las mejores ganancias Kp, Ki, Kd para la planta G(s) usando una
    malla logarítmica y el error compuesto. Devuelve el Top-N candidatos
    ordenados de menor a mayor error, ya validados contra una entrada
    escalón (no solo contra la señal usada para sintonizar).
    """
    Kp_range = np.logspace(np.log10(kp_range[0]), np.log10(kp_range[1]), n_por_eje)
    Ki_range = np.logspace(np.log10(ki_range[0]), np.log10(ki_range[1]), n_por_eje)
    Kd_range = np.logspace(np.log10(kd_range[0]), np.log10(kd_range[1]), n_por_eje)

    t = np.linspace(0, t_final, n_puntos)
    # Referencia suave para sintonizar: evita discontinuidades de derivada
    # que sesgarían la búsqueda hacia ganancias "buenas" solo para esa forma
    # de entrada, y no para un escalón real.
    ref_sintonizacion = 0.5 * (1 - np.cos(0.2 * t))

    Kp_grid, Ki_grid, Kd_grid = np.meshgrid(Kp_range, Ki_range, Kd_range, indexing="ij")
    combinaciones = np.vstack([Kp_grid.ravel(), Ki_grid.ravel(), Kd_grid.ravel()]).T

    raiz: NodoPID | None = None
    total = len(combinaciones)

    for i, (Kp, Ki, Kd) in enumerate(combinaciones):
        m = simular_lazo_cerrado(Kp, Ki, Kd, t, ref_sintonizacion, G)
        if np.isinf(m["error_compuesto"]):
            continue
        nodo = NodoPID(Kp, Ki, Kd, m["error_compuesto"], m["iae"], m["os"],
                        m["tr"], m["energia"], m["ess"])
        raiz = insertar_nodo(raiz, nodo)
        if verbose and i % max(1, total // 5) == 0:
            print(f"  Evaluando combinación {i + 1}/{total}")

    ordenados = recorrido_inorden(raiz)
    top = ordenados[:top_n]

    # Validación con entrada escalón (distinta a la de sintonización)
    ref_step = np.ones_like(t)
    resultados = []
    for nodo in top:
        y_step = simular_salida(nodo.Kp, nodo.Ki, nodo.Kd, t, ref_step, G)
        resultados.append({
            "Kp": nodo.Kp, "Ki": nodo.Ki, "Kd": nodo.Kd,
            "error_compuesto": nodo.error_compuesto, "iae": nodo.iae,
            "overshoot_pct": nodo.os, "tiempo_subida_s": nodo.tr,
            "energia_control": nodo.energia, "error_estacionario": nodo.ess,
            "t": t, "y_step": y_step, "ref_step": ref_step,
        })
    return resultados


# ──────────────────────────────────────────────────────────────────────────
# 5. Ejemplo de uso
# ──────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Planta de ejemplo: actuador industrial de segundo orden.
    # Sustituye estos coeficientes por el modelo identificado de tu planta.
    numerador = [8.73]
    denominador = [4.09e-6, 5.83e-3, 1.0]
    G = TransferFunction(numerador, denominador)

    print("Buscando ganancias PID (malla logarítmica + error compuesto)...")
    top3 = buscar_pid(G, n_por_eje=10)

    print("\nTop 3 PID según error compuesto:")
    for i, r in enumerate(top3, start=1):
        print(
            f"#{i}: Kp={r['Kp']:.4f}  Ki={r['Ki']:.4f}  Kd={r['Kd']:.4f}  "
            f"| error={r['error_compuesto']:.5f}  IAE={r['iae']:.4f}  "
            f"OS={r['overshoot_pct']:.2f}%  Tr={r['tiempo_subida_s']:.3f}s  "
            f"Energía={r['energia_control']:.3f}  Ess={r['error_estacionario']:.5f}"
        )

    # Descomenta para graficar el mejor candidato contra el escalón:
    #
    # import matplotlib.pyplot as plt
    # mejor = top3[0]
    # plt.plot(mejor["t"], mejor["ref_step"], "k--", label="Referencia (escalón)")
    # plt.plot(mejor["t"], mejor["y_step"], "r", label="Salida")
    # plt.xlabel("Tiempo [s]"); plt.ylabel("Salida"); plt.legend(); plt.grid(True)
    # plt.title(f"Mejor PID: Kp={mejor['Kp']:.3f}, Ki={mejor['Ki']:.3f}, Kd={mejor['Kd']:.3f}")
    # plt.show()
