# 🧪 Laboratorio: Predicción de Resistencia del Cemento - ATLAS FuzzyFrog.AI

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Colab](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E?logo=scikitlearn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-despliegue-009688?logo=fastapi&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/ATLAS-FuzzyFrog.AI-00b76c)

**Aprende a predecir un resultado de calidad industrial días antes de que esté disponible, sin dejar que el split de datos ni las variables relacionadas infle el resultado.**

## Qué vas a aprender

- A distinguir una variable que predice de una que solo es otra medición del mismo resultado, y a excluirla del entrenamiento aunque esté disponible en el CSV.
- A dividir datos de producción real por fecha, no al azar, cuando el modelo se va a usar hacia adelante en el tiempo.
- A medir la estabilidad de un modelo con bootstrap sin contaminar la evaluación con datos que el modelo ya vio.
- A empaquetar un modelo entrenado como una API real, sin credenciales escritas en el código.

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/prediccion-resistencia-cemento/) | [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
prediccion-resistencia-cemento/
├── README.md                              ← este archivo
├── resistencia_compresion_cemento.ipynb   ← notebook completo, corrido de principio a fin
├── diagrama-solucion.svg                  ← diagrama editable del pipeline (fuente, no imagen exportada)
└── requirements.txt                       ← dependencias con versión fija
```

Los datos no viven en este repositorio: el notebook los descarga en vivo desde un CSV público (`data_url` en la celda de carga de datos), así que no hace falta una carpeta `/data`.

## Enfoque de análisis

- 🕒 **División temporal, no aleatoria.** Con datos de producción real, un split aleatorio deja muestras del mismo lote repartidas entre entrenamiento y prueba, lo que infla artificialmente la métrica. Se ordena por fecha y se entrena con el pasado. Ver Bergmeir & Benítez, *"On the use of cross-validation for time series predictor evaluation"* (2012).
- 🎯 **Selección de variable objetivo entre mediciones relacionadas.** Cuando existen varias mediciones del mismo resultado en distintos momentos, ninguna puede ser predictora de las otras. Se excluyen explícitamente y se justifica, con datos, cuál conviene predecir.
- 🌲 **Random Forest sobre SVR y KNN, con validación cruzada honesta.** El conjunto de prueba se queda fuera de la selección de modelo y de la afinación, no solo del entrenamiento final. Ver Breiman, *"Random Forests"*, Machine Learning 45 (2001).
- 🔁 **Estabilidad con bootstrap sin fuga.** Cada réplica se entrena sobre un remuestreo del entrenamiento y se evalúa siempre contra el mismo conjunto de prueba nunca visto, para que la estabilidad reportada sea real, no una ilusión por evaluar contra datos ya conocidos. Ver Efron & Tibshirani, *"An Introduction to the Bootstrap"* (1993).

## Explora las decisiones alternativas

Cada una de estas decisiones se puede probar de forma interactiva en el artículo, antes de ver qué se decidió en el proyecto:

- **¿Dividir los datos al azar o por fecha?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/prediccion-resistencia-cemento/#explorador-division_datos)
- **¿Qué edad de resistencia predecir: 1 día o 28 días?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/prediccion-resistencia-cemento/#explorador-edad_resistencia)
- **¿Imputar los valores faltantes o eliminar las filas con nulos?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/prediccion-resistencia-cemento/#explorador-tratamiento_nulos)
- **¿Qué modelo base usar: Random Forest, SVR o KNN?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/prediccion-resistencia-cemento/#explorador-modelo_base)

## Metas

Al recorrer este repositorio vas a practicar:

- Diseñar una validación temporal correcta para datos de producción con fecha.
- Armar un `Pipeline` de scikit-learn donde ningún paso de preprocesamiento se ajuste con datos de prueba.
- Comparar modelos con validación cruzada sin reutilizar el mismo split para elegir y para confirmar.
- Escribir un checklist metodológico con aserciones que realmente corren, no solo texto narrativo.
- Empaquetar un modelo como API, manejando credenciales fuera del código.

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/prediccion-resistencia-cemento/)
- Bergmeir, C. & Benítez, J.M. (2012). *On the use of cross-validation for time series predictor evaluation.* Information Sciences.
- Breiman, L. (2001). *Random Forests.* Machine Learning, 45(1), 5-32.
- Efron, B. & Tibshirani, R.J. (1993). *An Introduction to the Bootstrap.* Chapman & Hall/CRC.
- **Referencias recientes sobre el mismo problema** «citadas en la sección de Limitaciones del artículo, no son trabajo propio»:
  - [Rapid on-site prediction of concrete compressive strength using integrated machine learning and non-destructive testing](https://link.springer.com/article/10.1007/s42107-026-01753-0) (2026).
  - Palanisamy et al. (2025). [Prediction of early age compressive strength of concrete using machine learning](https://www.nature.com/articles/s41598-025-29233-6). Scientific Reports, 15, 45293.
  - Nikoopayan Tak, M.S., Feng, Y. & Mahgoub, M. (2025). [Advanced Machine Learning Techniques for Predicting Concrete Compressive Strength](https://doi.org/10.3390/infrastructures10020026). Infrastructures, 10(2), 26.
- [`resistencia_compresion_cemento.ipynb`](./resistencia_compresion_cemento.ipynb) — el notebook completo

## Cómo usar

1. Clona el repositorio o descarga el notebook directamente.
2. Ábrelo en [Google Colab](https://colab.research.google.com/drive/1hYek_x8C4S2KICBoWcV9KMoDshnITht3?usp=sharing) o localmente con Jupyter, con las dependencias de `requirements.txt` instaladas.
3. Córrelo de principio a fin: los datos se descargan en vivo, no hace falta ningún archivo adicional.
4. Para probar la función de inferencia, corre las celdas de la sección 7 (Despliegue del modelo): levantan una API con FastAPI, la publican temporalmente con ngrok y envían una solicitud real de ejemplo.

---

Made with 💚 by FuzzyFrog.AI
