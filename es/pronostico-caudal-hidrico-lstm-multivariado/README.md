# 🧪 Laboratorio: Pronóstico de Caudal Hídrico con LSTM Multivariado - ATLAS FuzzyFrog.AI

**Aprenderás a construir un pronóstico de caudal con LSTM a partir de datos abiertos de gobierno, comparando arquitecturas y evaluando con las métricas estándar de hidrología.**

🔗 [Plataforma](https://fuzzyfrog.ai/es/) | 📄 [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/ambiente/pronostico-caudal-hidrico-lstm-multivariado/) | 📁 [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
pronostico-caudal-hidrico-lstm-multivariado/
├── pronostico-caudal-hidrico-lstm-multivariado.ipynb   # Notebook ejecutable: LSTM univariada, multivariada y multi-step
├── SubCuenca_SanMateo.csv                              # Datos hidrometeorológicos abiertos usados en el proyecto
├── README.md                                           # Este archivo
└── outputs/                                            # Modelos y resultados generados al ejecutar el notebook
```

## Enfoque de análisis

- 🌊 **LSTM para modelado lluvia-escorrentía**, capturando dependencias de largo plazo entre precipitación y caudal: Kratzert, F., Klotz, D., Brenner, C., Schulz, K., & Herrnegger, M. (2018). *Rainfall–runoff modelling using Long Short-Term Memory (LSTM) networks*. Hydrology and Earth System Sciences, 22(11), 6005-6022. [doi:10.5194/hess-22-6005-2018](https://doi.org/10.5194/hess-22-6005-2018).
- 📐 **Coeficiente de Nash-Sutcliffe como métrica estándar de evaluación hidrológica**, en vez de depender solo del error cuadrático medio genérico: Nash, J.E., & Sutcliffe, J.V. (1970). *River flow forecasting through conceptual models part I — A discussion of principles*. Journal of Hydrology, 10(3), 282-290.
- ⏱️ **Comparación contra una línea base autoregresiva y evaluación en varios horizontes de pronóstico**, en resolución horaria: *Evaluation of LSTM vs. conceptual models for hourly rainfall runoff simulations with varied training period lengths*, Scientific Reports (2025). [nature.com/articles/s41598-025-96577-4](https://www.nature.com/articles/s41598-025-96577-4).

## Metas

- Construir un pipeline de pronóstico de series de tiempo hidrológicas con LSTM, a partir de datos abiertos reales.
- Decidir con criterio cuándo usar rezagos uniformes y cuándo ajustar la ventana de tiempo por variable.
- Evaluar con métricas específicas de hidrología (Nash-Sutcliffe, BIAS, RMSE, r, r²), no solo con métricas genéricas de machine learning.
- Reportar con honestidad la diferencia de desempeño entre validación y prueba, en vez de ocultarla.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?logo=tensorflow&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- 🔗 [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- 📄 [Artículo completo con el diagrama del pipeline](https://fuzzyfrog.ai/es/ai-lab/proyectos/ambiente/pronostico-caudal-hidrico-lstm-multivariado/)
- 📚 Papers citados arriba (Kratzert et al. 2018, Nash & Sutcliffe 1970, Scientific Reports 2025)
- 📓 [`pronostico-caudal-hidrico-lstm-multivariado.ipynb`](./pronostico-caudal-hidrico-lstm-multivariado.ipynb)
- 🗂️ [`SubCuenca_SanMateo.csv`](./SubCuenca_SanMateo.csv)

## Cómo usar

1. Clona este repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre `pronostico-caudal-hidrico-lstm-multivariado.ipynb` en Jupyter o Google Colab.
3. Asegúrate de tener `SubCuenca_SanMateo.csv` en la misma carpeta que el notebook.
4. Corre el notebook celda por celda: carga de datos → EDA → modelado → evaluación con métricas hidrológicas.
5. Compara tus resultados contra las cifras de referencia del proyecto original que aparecen en la sección de evaluación.

---
*Made with ❤️ by FuzzyFrog.AI*
