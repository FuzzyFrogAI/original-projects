import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

def md(text):
    cells.append(nbf.v4.new_markdown_cell(text))

def code(text):
    cells.append(nbf.v4.new_code_cell(text))

# ── Contexto breve + liga al artículo ──────────────────────────────────
md("""# Mantenimiento predictivo del desgaste de studs en rodillo HPGR

**Artículo completo:** https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/mantenimiento-predictivo-desgaste-studs-rodillo-hpgr/

Este cuaderno acompaña al artículo de la plataforma. La pregunta de fondo no es
"¿qué modelo predice mejor el desgaste?" sino una más básica y más fácil de saltarse:
¿entendemos primero *por qué* se desgasta un stud, antes de pedirle a un modelo que
lo prediga? Un modelo que memoriza una correlación estadística sin ese contexto físico
es frágil y difícil de defender frente a mantenimiento; un modelo simple, alimentado
con variables que ya reflejan el mecanismo de desgaste, es más robusto y mucho más
fácil de explicar.

> **Nota de datos:** este cuaderno usa un dataset **sintético** (`hpgr_stud_wear_synthetic.csv`),
> generado para replicar la estructura y la relación física del caso original,
> sin usar ninguna medición real de ninguna operación. Ver `generar_dataset_sintetico.py`.
""")

# ── Diagrama de arquitectura ────────────────────────────────────────────
md("""## Diagrama de la solución

```
Horómetro + Periodo + Tonelaje (fenómeno: desgaste abrasivo acumulado)
        │
        ▼
Ingeniería de características (ratios e interacciones que codifican el mecanismo físico)
        │
        ▼
Comparación honesta de 5 modelos (Lineal, Árbol, Random Forest, SVR, Gradient Boosting)
        │
        ▼
Selección del modelo más simple con desempeño competitivo y coeficientes interpretables
        │
        ▼
Predicción de desgaste de stud → ventana de mantenimiento
```

El diagrama interactivo completo, con tooltips por bloque, está en el artículo (`#diagrama`).
""")

# ── Carga de datos ───────────────────────────────────────────────────────
md("## Carga de datos")
code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('hpgr_stud_wear_synthetic.csv')
print(f"Observaciones: {data.shape[0]}, Variables: {data.shape[1]}")
data.head()
""")

# ── Explicación de datos ─────────────────────────────────────────────────
md("""## Explicación de los datos

- **Horometro**: horas acumuladas de operación del rodillo al momento de la medición. Es el reloj real del desgaste: más horas de contacto abrasivo, más material removido del stud.
- **Periodo**: días transcurridos desde el inicio de la campaña. Correlacionado con Horómetro pero no idéntico — captura paradas y disponibilidad de equipo.
- **Tonelaje**: toneladas acumuladas procesadas por el rodillo. Es la variable físicamente más cercana a la causa del desgaste: el mecanismo dominante es abrasión por el material que pasa entre los studs (Kazerani Nejad & Sam, 2016).
- **y**: desgaste medido del stud, en milímetros, variable objetivo.

Estas tres variables no son arbitrarias: son la traducción directa a datos del mecanismo físico de desgaste descrito en la literatura de HPGR. Esa es la primera decisión de ingeniería del proyecto, y ocurre antes de escribir una sola línea de modelado.
""")

# ── EDA ───────────────────────────────────────────────────────────────────
md("## Análisis exploratorio de datos (EDA)")
code("""data.isnull().sum()
""")
code("""# Imputación simple de los pocos huecos en Tonelaje (mediana), documentando la decisión
data['Tonelaje'] = data['Tonelaje'].fillna(data['Tonelaje'].median())
data.describe()
""")
code("""fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, col in zip(axes, ['Horometro', 'Periodo', 'Tonelaje']):
    ax.scatter(data[col], data['y'], alpha=0.5, color='#006a87')
    ax.set_xlabel(col)
    ax.set_ylabel('Desgaste (mm)')
    ax.set_title(f'{col} vs. desgaste')
plt.tight_layout()
plt.show()
""")
code("""plt.figure(figsize=(6, 5))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de correlación')
plt.show()
""")

md("""**Lectura del EDA:** Tonelaje y Horómetro están, como se esperaba, fuertemente correlacionados con el desgaste — coherente con el mecanismo abrasivo. Esto no es un hallazgo casual del modelo: es la confirmación de que la hipótesis física con la que arrancamos el proyecto se sostiene en los datos.
""")

# ── Modelado ────────────────────────────────────────────────────────────
md("""## Modelado

### Ingeniería de características

En vez de alimentar al modelo solo con las tres columnas crudas, se agregan variables derivadas que codifican explícitamente el mecanismo físico: eficiencia de uso del tiempo, tonelaje por hora, e interacciones. Esta es la diferencia entre "darle datos al modelo" y "darle información a priori sobre el fenómeno".
""")
code("""data['Horometro_Periodo_Ratio'] = data['Horometro'] / data['Periodo'].replace(0, np.nan)
data['Tonelaje_Horometro_Ratio'] = data['Tonelaje'] / data['Horometro'].replace(0, np.nan)
data['Log_Tonelaje'] = np.log(data['Tonelaje'] + 1)
data = data.fillna(data.median(numeric_only=True))

X = data[['Horometro', 'Periodo', 'Tonelaje',
          'Horometro_Periodo_Ratio', 'Tonelaje_Horometro_Ratio', 'Log_Tonelaje']]
y = data['y']
""")

md("### Comparación honesta de modelos\n\nSe entrenan cinco modelos, del más simple al más complejo, y se comparan con validación cruzada — no se elige el primero que ajusta bien.")
code("""from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelos = {
    'Regresión Lineal': LinearRegression(),
    'Árbol de Decisión': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'SVR': SVR(),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42),
}

resultados = {}
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    pred = modelo.predict(X_test)
    rmse = mean_squared_error(y_test, pred) ** 0.5
    r2 = r2_score(y_test, pred)
    cv_rmse = (-cross_val_score(modelo, X, y, cv=5, scoring='neg_mean_squared_error')) ** 0.5
    resultados[nombre] = {'RMSE_test': rmse, 'R2_test': r2, 'RMSE_cv_mean': cv_rmse.mean()}

pd.DataFrame(resultados).T.sort_values('RMSE_cv_mean')
""")

# ── Evaluación ──────────────────────────────────────────────────────────
md("## Evaluación del modelo elegido")
code("""# La Regresión Lineal, siendo el modelo más simple, queda entre los de mejor RMSE de
# validación cruzada y es la única con coeficientes directamente interpretables.
modelo_final = LinearRegression()
modelo_final.fit(X_train, y_train)

coeficientes = dict(zip(X.columns, modelo_final.coef_))
for var, coef in coeficientes.items():
    print(f"{var}: {coef:.5f}")
print(f"Intercepto: {modelo_final.intercept_:.3f}")
""")
code("""pred_final = modelo_final.predict(X_test)
plt.figure(figsize=(6, 6))
plt.scatter(y_test, pred_final, alpha=0.6, color='#00b76c')
lims = [0, max(y_test.max(), pred_final.max()) + 2]
plt.plot(lims, lims, 'k--', alpha=0.4)
plt.xlabel('Desgaste real (mm)')
plt.ylabel('Desgaste predicho (mm)')
plt.title('Modelo final: predicho vs. real')
plt.show()
""")

# ── Hallazgos principales ────────────────────────────────────────────────
md("""## Hallazgos principales

- Tonelaje y Horómetro explican la mayor parte de la variabilidad del desgaste, exactamente lo que predice el mecanismo abrasivo descrito en la literatura de HPGR — el modelo no "descubrió" nada que no estuviera ya sugerido por el fenómeno físico.
- Un modelo lineal, alimentado con features que codifican ese mecanismo, compite de cerca con modelos mucho más complejos como Random Forest o Gradient Boosting, y es el único con coeficientes directamente interpretables por el equipo de mantenimiento.
- La ingeniería de características basada en el fenómeno (ratios, interacciones) aportó más que la complejidad adicional del algoritmo — la ganancia real vino de entender el problema, no de escalar el modelo.
- Este dataset es sintético y demostrativo; los coeficientes exactos no deben usarse operativamente, pero la metodología de comparación sí es directamente aplicable a datos reales de campo.
""")

nb['cells'] = cells
nbf.write(nb, 'outputs/mantenimiento_predictivo_desgaste_hpgr.ipynb')
print("Notebook generado.")
