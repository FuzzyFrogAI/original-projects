# 🧪 Laboratorio: Optimización de Controles Operativos en Minería con Clasificación Multietiqueta - ATLAS FuzzyFrog.AI

**Aprende a predecir decenas de controles operativos binarios a la vez, y a evaluar el resultado en dos capas para saber no solo qué tan bien acertó el modelo, sino dónde y cómo se equivocó.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/optimizacion-controles-operativos-mineria-machine-learning/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
optimizacion-controles-operativos-mineria-machine-learning/
├── optimizacion-controles-operativos-mineria-machine-learning.ipynb   # Notebook: carga, agrupación, 5 modelos y evaluación en 2 capas
├── data/
│   └── controles_operativos.csv   # Datos de ejemplo, sustituir por datos propios con autorización
└── README.md
```

## Enfoque de análisis

- ✅ **Variables binarias tratadas como preguntas, no como números.** Tasas de cumplimiento en vez de promedios genéricos. Referencia: Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- 🏷️ **Clasificación multietiqueta con `MultiOutputClassifier`, no un modelo binario por control.** Referencia: Tsoumakas, G., & Katakis, I. (2007). Multi-Label Classification: An Overview. *International Journal of Data Warehousing and Mining, 3*(3), 1-13.
- 🧩 **Agrupar por tipo de roca y tipo de labor antes de modelar**, en vez de tratar todas las tareas como un solo contexto. Referencia: Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
- 🔍 **Evaluación en dos capas: métricas globales más matriz de error por control específico.** Referencia: Huang, S., Hu, W., Lu, B., Fan, Q., Xu, X., Zhou, X., & Yan, H. (2024). Application of Label Correlation in Multi-Label Classification: A Survey. *Applied Sciences, 14*(19), 9034.

## Metas

- Practicar el tratamiento correcto de variables binarias, tanto en análisis exploratorio como en modelado.
- Aprender a usar `MultiOutputClassifier` de scikit-learn para predecir varias etiquetas relacionadas a la vez.
- Ver un ejemplo real de por qué agrupar antes de modelar cambia qué algoritmo termina ganando.
- Entender por qué una métrica global nunca es suficiente en un contexto operativo, y cómo construir una segunda capa de evaluación por variable.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-MultiOutputClassifier-F7931E?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Análisis%20de%20datos-150458?logo=pandas&logoColor=white)
![Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/optimizacion-controles-operativos-mineria-machine-learning/)
- Papers citados en "Enfoque de análisis" arriba
- `optimizacion-controles-operativos-mineria-machine-learning.ipynb` (notebook principal)

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Sustituye `data/controles_operativos.csv` por tus propios registros, manteniendo el mismo esquema de columnas (una columna por control binario, más zona, guardia, operador, tipo de roca, tipo de labor y avance).
3. Abre `optimizacion-controles-operativos-mineria-machine-learning.ipynb` en Jupyter o Google Colab.
4. Corre las celdas en orden: carga de datos → agrupación por roca y labor → EDA → los 5 modelos multietiqueta → evaluación en 2 capas.
5. Para priorizar qué controles revisar primero, ordena la tabla de `matriz_error_por_control` por `falsos_negativos` de mayor a menor.

---
*Made with ❤️ by FuzzyFrog.AI*
