# 🧪 Laboratorio: Predicción de Esquema de Vacunación Incompleto - ATLAS FuzzyFrog.AI

**Aprende a seleccionar variables con pruebas de hipótesis y corrección por comparaciones múltiples, en vez de confiar en la importancia de un solo modelo, y a balancear datos mixtos con SMOTENC.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/prediccion-esquema-vacunacion-incompleto-seleccion-estadistica/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
prediccion-esquema-vacunacion-incompleto-seleccion-estadistica/
├── prediccion-esquema-vacunacion-incompleto-seleccion-estadistica.ipynb   # Notebook principal: selección estadística, SMOTENC, comparación de modelos
├── outputs/
│   └── vacunacion_sintetico.csv   # Dataset sintético: variables demográficas/administrativas + esquema completo/incompleto
└── README.md                       # Este archivo
```

## Enfoque de análisis

- 📊 **Selección de variables con pruebas de hipótesis y corrección FDR.** Mann-Whitney U para numéricas, Chi-cuadrada + Cramér's V para categóricas, ajustadas por comparaciones múltiples antes de decidir qué variables entran al modelo. Referencia: Benjamini, Y., & Hochberg, Y. (1995). *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*. Journal of the Royal Statistical Society: Series B, 57(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x

- 🕰️ **Revisión de estabilidad temporal del objetivo antes de modelar.** Se mide si la proporción de esquemas completos cambia de forma importante entre periodos, para no tratar todo el histórico como una sola distribución sin verificarlo. Referencia: Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). *A Survey on Concept Drift Adaptation*. ACM Computing Surveys, 46(4), 1–37. https://doi.org/10.1145/2523813

- ⚖️ **Balance de clases con SMOTENC para datos mixtos.** A diferencia de SMOTE estándar, genera ejemplos sintéticos coherentes cuando el dataset combina variables numéricas y categóricas. Referencia: Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). *SMOTE: Synthetic Minority Over-sampling Technique*. Journal of Artificial Intelligence Research, 16, 321–357. https://doi.org/10.1613/jair.953

- 🎯 **Optimización bayesiana de hiperparámetros con Optuna.** Sobre el modelo campeón, usando peso balanceado por clase dado el desbalance del problema. Referencia: Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). *Optuna: A Next-generation Hyperparameter Optimization Framework*. https://arxiv.org/abs/1907.10902

## Metas

- Practicar selección de variables con pruebas de hipótesis (Mann-Whitney U, Chi-cuadrada) y corrección FDR
- Revisar estabilidad temporal de una variable objetivo antes de confiar en todo el histórico disponible
- Balancear datasets con variables numéricas y categóricas mezcladas usando SMOTENC
- Comparar modelos de clasificación con AUC y afinar el campeón con optimización bayesiana

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-scikit--learn%20%7C%20XGBoost%20%7C%20Optuna-F7931E)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + discusión de estabilidad temporal): https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/prediccion-esquema-vacunacion-incompleto-seleccion-estadistica/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `prediccion-esquema-vacunacion-incompleto-seleccion-estadistica.ipynb` y `outputs/vacunacion_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `prediccion-esquema-vacunacion-incompleto-seleccion-estadistica.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/vacunacion_sintetico.csv`.
4. Para probar el pipeline con tu propio registro, respeta la separación entre columnas numéricas y categóricas, y ajusta la lista `num_cols` / `cat_cols` en la sección de selección de variables antes de correr desde ahí en adelante.

---

*Made with ❤️ by FuzzyFrog.AI*
