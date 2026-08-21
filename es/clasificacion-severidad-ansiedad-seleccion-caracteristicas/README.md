# 🧪 Laboratorio: Clasificación de Severidad de Ansiedad - ATLAS FuzzyFrog.AI

**Aprende a comparar de forma sistemática varios métodos de selección de características contra varias familias de clasificadores, y por qué balancear las clases antes de comparar es tan importante como el modelo mismo.**

⚠️ **Nota importante:** este laboratorio es un ejercicio de investigación y aprendizaje sobre datos autorreportados. No es una herramienta de diagnóstico ni un instrumento clínico validado.

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-severidad-ansiedad-seleccion-caracteristicas/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
clasificacion-severidad-ansiedad-seleccion-caracteristicas/
├── clasificacion-severidad-ansiedad-seleccion-caracteristicas.ipynb   # Notebook principal: balance de clases, barrido de selección de features
├── outputs/
│   └── ansiedad_sintetico.csv   # Dataset sintético: escalas psicométricas, demografía y severidad
└── README.md                     # Este archivo
```

## Enfoque de análisis

- 🧹 **Exclusión explícita del puntaje crudo de la variable objetivo.** Dejar la fuente de la que se deriva la etiqueta como feature es una fuga de información que infla artificialmente el desempeño reportado. Referencia: Kaufman, S., Rosset, S., & Perlich, C. (2012). *Leakage in Data Mining: Formulation, Detection, and Avoidance*. ACM Transactions on Knowledge Discovery from Data, 6(4). https://doi.org/10.1145/2382577.2382579

- ⚖️ **Balance de clases con sobremuestreo y submuestreo antes de comparar modelos.** La clase de severidad grave es minoritaria; sin balancear, un modelo puede lograr accuracy alto sin aprender nada útil sobre ella. Referencia: Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). *SMOTE: Synthetic Minority Over-sampling Technique*. Journal of Artificial Intelligence Research, 16, 321–357. https://doi.org/10.1613/jair.953

- 🔍 **Comparación sistemática de métodos de selección de características, no uno elegido a priori.** Distintos métodos de ranking de importancia interactúan de forma distinta con cada clasificador; probar varias combinaciones evita apostar por una que solo suena razonable. Referencia: Guyon, I., & Elisseeff, A. (2003). *An Introduction to Variable and Feature Selection*. Journal of Machine Learning Research, 3, 1157–1182.

- 🎯 **Afinación de hiperparámetros solo sobre el modelo campeón.** Búsqueda aleatoria seguida de búsqueda en grilla, en vez de afinar cada combinación del barrido, un uso más razonable del tiempo de cómputo. Referencia: Bergstra, J., & Bengio, Y. (2012). *Random Search for Hyper-Parameter Optimization*. Journal of Machine Learning Research, 13, 281–305.

## Metas

- Practicar la detección y prevención de fuga de información en variables derivadas del objetivo
- Aplicar técnicas de balance de clases (SMOTE + submuestreo) antes de comparar modelos
- Comparar de forma sistemática métodos de selección de características contra varias familias de clasificadores
- Reconocer los límites de un modelo entrenado sobre datos autorreportados y comunicarlos con honestidad

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-scikit--learn%20%7C%20imbalanced--learn-F7931E)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + discusión sobre límites del modelo): https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-severidad-ansiedad-seleccion-caracteristicas/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `clasificacion-severidad-ansiedad-seleccion-caracteristicas.ipynb` y `outputs/ansiedad_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `clasificacion-severidad-ansiedad-seleccion-caracteristicas.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/ansiedad_sintetico.csv`.
4. Para probar el barrido con tus propias variables, respeta el formato de columnas (features + `outcome`) y vuelve a correr desde la sección de modelado; el balance de clases y el barrido de selección de características se recalculan automáticamente.

---

*Made with ❤️ by FuzzyFrog.AI*
