# 🧪 Laboratorio: Predicción de deserción estudiantil con Machine Learning - ATLAS FuzzyFrog.AI

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Colab](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E?logo=scikitlearn&logoColor=white)
![imbalanced-learn](https://img.shields.io/badge/imbalanced--learn-0.14.2-006a87)
![SHAP](https://img.shields.io/badge/SHAP-0.52.0-00b76c)
![ATLAS](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-001f3d)

**Aprende a construir un sistema de alerta temprana de deserción que no se engaña a sí mismo: decidir con evidencia qué variables existen a tiempo, evaluar sin fugas de datos y explicar cada alerta.**

## Qué vas a aprender

- A separar una variable que predice de una que solo describe el desenlace ya ocurrido, y a medir cuánto AUC cuesta alertar a tiempo.
- A elegir la métrica correcta con clases desbalanceadas, en lugar de confiar en el Accuracy.
- A interpretar un modelo de caja negra con SHAP, a nivel global e individual.

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/modelado-retencion-estudiantil/) | [Todos los proyectos](https://fuzzyfrog.ai/es/ai-lab/proyectos/)

## Estructura del laboratorio

```
modelado-retencion-estudiantil/
├── README.md                                  Presentación del laboratorio
├── modelado_retencion_estudiantil.ipynb       Notebook completo: del dataset al modelo explicado
├── diagrama-solucion.svg                      Fuente editable del diagrama de la solución, con texto accesible
└── requirements.txt                           Dependencias con versión para reproducir el entorno
```

El dataset no se versiona: el notebook lo descarga en vivo desde el repositorio de la UCI.

## Enfoque de análisis

- 🕒 **Corte temporal de variables.** Se compara el mismo modelo con todas las variables y solo con las que existen antes del 2do semestre, para que la alerta sea temprana de verdad y no una descripción del desenlace. Referencia: Kaufman, S., Rosset, S., Perlich, C. y Stitelman, O. (2012). Leakage in data mining: formulation, detection, and avoidance. ACM Transactions on Knowledge Discovery from Data, 6(4).
- ⚖️ **SMOTE dentro del Pipeline.** El sobremuestreo sintético se aplica solo al fold de entrenamiento de cada iteración, junto con el escalado y el modelo, para que la validación cruzada no quede inflada. Referencia: Chawla, N. V., Bowyer, K. W., Hall, L. O. y Kegelmeyer, W. P. (2002). SMOTE: Synthetic Minority Over-sampling Technique. Journal of Artificial Intelligence Research, 16, 321 a 357.
- 🎯 **Umbral con la curva precisión-recall.** El punto de corte de la alerta se elige con validación, nunca con test, porque con clases desbalanceadas la curva precisión-recall es más informativa que la ROC. Referencia: Saito, T. y Rehmsmeier, M. (2015). The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets. PLoS ONE, 10(3).
- 🔍 **Interpretabilidad con SHAP.** Cada predicción se reparte entre las variables para saber por qué se lanzó una alerta. Referencia: Lundberg, S. M. y Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. Advances in Neural Information Processing Systems, 30.

## Explora las decisiones alternativas

Cada decisión del notebook tiene una alternativa descartada. Pruébala en el Explorador de decisiones del artículo y mira qué habría pasado.

1. ¿Predecir con todas las variables o solo con las que existen antes del 2do semestre? [Explorar](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/modelado-retencion-estudiantil/#explorador-corte_temporal)
2. ¿Sin balanceo, con peso de clase o con SMOTE? [Explorar](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/modelado-retencion-estudiantil/#explorador-manejo_desbalance)
3. ¿Escalar una vez sobre todo train o dentro de cada fold de validación cruzada? [Explorar](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/modelado-retencion-estudiantil/#explorador-escalado_sin_fuga)
4. ¿Elegir el modelo por Accuracy, por Recall o por AUC? [Explorar](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/modelado-retencion-estudiantil/#explorador-metrica_seleccion)
5. ¿Umbral fijo de 0.5 o un umbral ajustado con la curva precisión-recall? [Explorar](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/modelado-retencion-estudiantil/#explorador-umbral_alerta)

## Metas

- Construir un pipeline de clasificación donde el escalado, el balanceo y la selección de umbral se ajustan solo con información de entrenamiento o validación.
- Comparar cinco modelos con validación cruzada y afinar el mejor con GridSearchCV.
- Distinguir un modelo útil de un modelo trampa con Recall y AUC, no con Accuracy.
- Evaluar en el conjunto de prueba una sola vez y leer el resultado en dos capas: técnica e institucional.
- Explicar con SHAP qué empuja cada predicción hacia la deserción o hacia la graduación.
- Verificar con aserciones que corren de verdad que no hay fuga de datos.

## Recursos

- [Plataforma ATLAS FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/modelado-retencion-estudiantil/)
- Dataset: Realinho, V., Machado, J., Baptista, L. y Martins, M. V. (2022). Predicting Student Dropout and Academic Success. Data, 7(11), 146. Disponible en el [repositorio de la UCI](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success).
- Papers citados en el enfoque de análisis: Kaufman et al. (2012), Chawla et al. (2002), Saito y Rehmsmeier (2015) y Lundberg y Lee (2017).
- Notebook: `modelado_retencion_estudiantil.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git` y entra a `es/modelado-retencion-estudiantil`.
2. Abre el notebook en [Google Colab](https://colab.research.google.com/drive/1RmvSYcS_LfvkEbFthkWRXdGz0OEuShCo?usp=sharing) o localmente con `pip install -r requirements.txt` y `jupyter notebook`.
3. Ejecuta todas las celdas en orden. El notebook descarga el dataset y termina con un checklist metodológico que debe decir que todas las verificaciones pasaron.
4. Abre el Explorador de decisiones del artículo y prueba las alternativas de cada decisión.

---

Made with 💚 by FuzzyFrog.AI
