# 🧪 Laboratorio: Identificación de Hurto de Energía con Clustering y Random Forest - ATLAS FuzzyFrog.AI

**Objetivo:** aprender a priorizar candidatos de inspección de hurto de energía a partir del comportamiento de una serie de tiempo de consumo, no de su nivel absoluto.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/identificacion-hurto-energia-clustering-random-forest/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
identificacion-hurto-energia-clustering-random-forest/
├── identificacion-hurto-energia-clustering-random-forest.ipynb   # Notebook ejecutable, extremo a extremo
├── outputs/
│   └── dataset_sintetico_consumo.csv                              # Dataset sintético (consumo mensual por servicio)
└── README.md                                                      # Este archivo
```

## Enfoque de análisis

- 📈 **Tendencia como característica principal.** Más que la media o el máximo de consumo, la pendiente de la serie de tiempo (calculada con una regresión lineal simple) es la señal que mejor separa una caída sostenida por manipulación de un consumo naturalmente bajo. Referencia: Nizar, A. H., Dong, Z. Y., Jalaluddin, M., & Raffles, M. J. (2006). *Load profiling method in detecting non-technical loss activities in a power utility.* First International Power and Energy Conference (PECon), 82–87. https://doi.org/10.1109/PECON.2006.346624
- 🌳 **Random Forest para la clasificación supervisada.** Se eligió sobre un solo árbol de decisión por su menor varianza y su capacidad de reportar importancia de características, clave para validar que la tendencia domina la decisión del modelo. Referencia: Breiman, L. (2001). *Random Forests.* Machine Learning, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324
- ⚖️ **SMOTE para el desbalance de clases.** Con ~13% de servicios etiquetados como hurto, entrenar sin corrección produce un modelo que ignora la clase minoritaria. SMOTE se aplica únicamente sobre el conjunto de entrenamiento, después del split, para no filtrar información sintética hacia la evaluación. Referencia: Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). *SMOTE: Synthetic Minority Over-sampling Technique.* Journal of Artificial Intelligence Research, 16, 321–357. https://doi.org/10.1613/jair.953
- 🔍 **K-Means como exploración, no como solución.** Se usó para caracterizar el comportamiento de consumo sin la etiqueta real, y ese mismo ejercicio reveló su límite: agrupa antes por magnitud de consumo (tarifa) que por patrón de hurto. Referencia: MacQueen, J. (1967). *Some methods for classification and analysis of multivariate observations.* Proceedings of the 5th Berkeley Symposium on Mathematical Statistics and Probability, 1, 281–297.

## Metas

- Practicar ingeniería de características sobre series de tiempo para un problema de clasificación tabular.
- Entender por qué corregir el desbalance de clases (SMOTE + pesos de clase) no es opcional cuando la clase de interés es minoritaria.
- Aprender a leer un reporte de clasificación desbalanceado: por qué el accuracy engaña y el recall de la clase de interés es la métrica que importa.
- Ver, con un caso concreto, dónde el clustering no supervisado deja de ser suficiente y hace falta una etiqueta real.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![imbalanced-learn](https://img.shields.io/badge/imbalanced--learn-SMOTE-00b76c)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-006a87)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del caso](https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/identificacion-hurto-energia-clustering-random-forest/)
- Papers citados arriba en *Enfoque de análisis*
- [`identificacion-hurto-energia-clustering-random-forest.ipynb`](./identificacion-hurto-energia-clustering-random-forest.ipynb)

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `identificacion-hurto-energia-clustering-random-forest.ipynb` en Jupyter, Google Colab o VS Code.
3. Ejecuta todas las celdas en orden; el dataset sintético se genera dentro del propio notebook, no requiere descargas externas.
4. Para probar el modelo con tus propios datos, reemplaza la celda de generación de datos por la carga de tu propio histórico de consumo, manteniendo las columnas `IdNroServicio`, `Periodo`, `ConsumoEAT` y `Hurtos`.

---
*Made with ❤️ by FuzzyFrog.AI*
