# Sintonización de controladores PID con error compuesto y árbol binario

Caso de estudio de [FuzzyFrog.AI](https://fuzzyfrog.ai/es/ai-lab/proyectos/) — proyectos de IA aplicada a industria.

## El problema

Sintonizar un controlador PID (`Kp`, `Ki`, `Kd`) por prueba y error, o incluso con
Ziegler-Nichols, casi nunca da el mejor compromiso entre velocidad de respuesta,
sobreimpulso y esfuerzo de control. Una búsqueda heurística (malla logarítmica,
Algoritmo Genético, Evolución Diferencial, etc.) puede explorar el espacio de
ganancias, pero **si la función objetivo es solo el error cuadrático medio
(MSE), el "óptimo" que encuentra puede oscilar o exigir un esfuerzo de control
poco realista para un actuador físico.**

## El hallazgo

La función objetivo importa más que el algoritmo de búsqueda. Este proyecto
compone el error con seis criterios en vez de uno:

- **IAE** — integral del error absoluto
- **Overshoot (%)**
- **Tiempo de subida**
- **Energía de la señal de control** (∫|u| dt)
- **Error en estado estacionario**
- **Penalización de oscilaciones** (cruces con la referencia)

Los candidatos se insertan en un **árbol binario ordenado por error
compuesto**: el recorrido inorden entrega el ranking completo, y la estructura
queda lista para una búsqueda incremental (por ejemplo, si más adelante
quieres alimentar generaciones de un Algoritmo Genético sin reprocesar todo
desde cero).

## Contenido del repositorio

```
sintonizacion_pid.py   # Pipeline completo: álgebra de TF, árbol binario,
                        # error compuesto, búsqueda en malla y validación
requirements.txt       # Dependencias
README.md              # Este archivo
```

## Cómo correrlo

```bash
pip install -r requirements.txt
python sintonizacion_pid.py
```

Sustituye el numerador/denominador de `G` en el bloque `if __name__ ==
"__main__":` por el modelo identificado de tu propia planta (motor, lazo de
temperatura, nivel de tanque, banda transportadora, etc.). El script imprime
el Top-3 de combinaciones `Kp, Ki, Kd` con sus métricas, ya validadas contra
una entrada escalón distinta a la señal usada para sintonizar.

## Versión interactiva (sin instalar nada)

Hay una versión de este mismo motor de búsqueda corriendo 100% en el
navegador (JavaScript, sin backend), donde puedes meter los coeficientes de
tu propia planta y obtener las ganancias recomendadas al instante:
[fuzzyfrog.ai/es/ai-lab/proyectos/industria/sintonizacion-pid-error-compuesto-arbol-binario](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/sintonizacion-pid-error-compuesto-arbol-binario/)

## Referencias

- Saad, M. S., Jamaluddin, H., & Darus, I. Z. M. (2012). *Implementation of
  PID controller tuning using differential evolution and genetic
  algorithms.* International Journal of Innovative Computing, Information
  and Control, 8(11), 7761–7779.
- de Moura, J. P., da Fonseca Neto, J. V., & Rêgo, P. H. M. (2020). *A
  Neuro-Fuzzy Model for Online Optimal Tuning of PID Controllers in
  Industrial System Applications to the Mining Sector.* IEEE Transactions
  on Fuzzy Systems, 28(8), 1864–1877. https://doi.org/10.1109/TFUZZ.2019.2923963
- Joseph, S. B., Dada, E. G., Abidemi, A., Oyewola, D. O., & Khammas, B. M.
  (2022). *Metaheuristic algorithms for PID controller parameters tuning:
  review, approaches and open problems.* Heliyon, 8(5), e09399.
  https://doi.org/10.1016/j.heliyon.2022.e09399

## Licencia y uso

Código de referencia con fines educativos, pensado como punto de partida
para tesis y proyectos aplicados. Antes de llevarlo a un controlador físico,
valida el modelo de planta con datos reales y respeta los límites de
seguridad de tu actuador (saturación, límites de energía, anti-windup).
