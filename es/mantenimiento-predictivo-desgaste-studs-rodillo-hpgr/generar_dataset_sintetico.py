"""
Dataset SINTÉTICO — Mantenimiento predictivo de desgaste de studs en rodillo HPGR
==================================================================================
Este dataset es DEMOSTRATIVO. No contiene mediciones reales de ninguna operación
minera. Fue generado para replicar la estructura, los tipos de dato y la relación
física del problema original (Horómetro, Periodo, Tonelaje -> desgaste de stud),
en un tamaño reducido, para fines educativos del artículo de la plataforma.

Fundamento físico simulado (ver paper de respaldo: Kazerani Nejad & Sam, 2016,
"The wear pattern in high pressure grinding rolls"): el desgaste de un stud crece
de forma aproximadamente proporcional al tonelaje procesado y al tiempo de
operación acumulado (horómetro), con una componente de ruido de medición y una
ligera no linealidad por el efecto de compactación del lecho de material entre
studs a medida que estos se desgastan.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

N = 180  # tamaño reducido, similar orden de magnitud a la muestra original (184)

# Horómetro acumulado de operación (horas), creciente con saltos irregulares
horometro = np.sort(rng.uniform(0, 11000, N))

# Periodo transcurrido en días desde el inicio de campaña, correlacionado con horometro
periodo = horometro / 24 * rng.uniform(0.8, 1.3, N)
periodo = np.round(periodo).astype(int)
periodo = np.clip(periodo, 0, None)

# Tonelaje procesado acumulado, proporcional al horómetro con variabilidad operativa
tasa_ton_hora = rng.normal(180, 25, N)  # ton/hr promedio de planta
tonelaje = horometro * tasa_ton_hora * rng.uniform(0.9, 1.1, N)
tonelaje = np.round(tonelaje, 1)

# Desgaste del stud (mm), variable objetivo 'y'
# Componente física: proporcional al tonelaje acumulado (mecanismo abrasivo dominante,
# ver Kazerani Nejad & Sam 2016), con una leve componente no lineal por el efecto de
# compactación del lecho de material entre studs a medida que estos se desgastan.
# Un stud típico tiene ~65 mm de altura y se retira del servicio cerca de 40-45 mm
# de desgaste (dejando el mínimo de 15 mm de vástago que exige el criterio de
# mantenimiento), así que la escala del coeficiente se calibra a ese rango.
tonelaje_norm = tonelaje / tonelaje.max()
desgaste_base = 38 * tonelaje_norm + 4 * (tonelaje_norm ** 1.6)
ruido_medicion = rng.normal(0, 1.4, N)  # ruido de instrumento (vernier / regleta)
y = desgaste_base + ruido_medicion
y = np.clip(y, 0, 48)

data = pd.DataFrame({
    "Horometro": np.round(horometro, 1),
    "Periodo": periodo,
    "Tonelaje": tonelaje,
    "y": np.round(y, 3),
})

# Inyectar unos pocos huecos, como en el registro original, para que el notebook
# muestre el manejo de datos faltantes de forma honesta
huecos_idx = rng.choice(data.index, size=4, replace=False)
data.loc[huecos_idx, "Tonelaje"] = np.nan

data.to_csv("outputs/hpgr_stud_wear_synthetic.csv", index=False)
print(data.describe())
print("\nDataset sintético guardado en outputs/hpgr_stud_wear_synthetic.csv")
print("NOTA: dataset 100% demostrativo, no contiene datos reales de ninguna operación.")
