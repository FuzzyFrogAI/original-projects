# 🧪 Laboratorio: Predicción de Variables de Tanques de Piscicultura con IoT - ATLAS FuzzyFrog.AI

**Objetivo:** aprender a diseñar un pipeline de predicción a corto plazo para sensores IoT, empezando por la hoja de datos del sensor y terminando en una alerta de recambio de agua que no depende por completo del modelo.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/agritech/prediccion-variables-tanque-piscicultura-iot-machine-learning/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
prediccion-variables-tanque-piscicultura-iot-machine-learning/
├── prediccion-variables-tanque-piscicultura-iot-machine-learning.ipynb   # Notebook ejecutable, extremo a extremo
├── outputs/
│   └── dataset_sintetico_tanque_piscicultura.csv                          # Dataset sintético (sensores del tanque, 15 min)
└── README.md                                                              # Este archivo
```

## Enfoque de análisis

- 📶 **MQTT como protocolo de comunicación del sensor.** Antes de diseñar el modelo, se revisó cómo publica el sensor (frecuencia, formato del payload), porque el protocolo de transporte define la cadencia real de datos disponibles para cualquier modelo. Referencia: OASIS Standard (2014). *MQTT Version 3.1.1.* https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html
- 🌳 **Random Forest para el horizonte corto (15-30 min).** Se prefirió sobre modelos de secuencia más complejos por su tolerancia a huecos de datos y su bajo costo de reentrenamiento, clave en un entorno de sensores de bajo costo con conexión intermitente. Referencia: Breiman, L. (2001). *Random Forests.* Machine Learning, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324
- 📉 **SARIMA como candidato para el ciclo diario, evaluado y descartado con evidencia.** La metodología Box-Jenkins es la referencia clásica para series estacionales, pero en este caso resultó frágil ante los huecos de datos interpolados y perdió frente a alternativas más simples. Referencia: Box, G. E. P., & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control.* Holden-Day.
- ⚠️ **Reglas de umbral independientes del modelo, como capa de seguridad.** Un sistema que solo alerta a partir de una predicción de machine learning falla en silencio si el modelo se degrada. Separar la lógica de alerta de la lógica de predicción es un principio de diseño de sistemas seguros. Referencia: Leveson, N. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety.* MIT Press.

## Metas

- Practicar el hábito de revisar las restricciones del sensor (resolución, latencia, frecuencia) antes de diseñar cualquier modelo de predicción sobre datos de IoT.
- Aprender a correr y leer un benchmark comparativo de modelos de series de tiempo con distinta complejidad, incluyendo cuándo un modelo "teóricamente mejor" falla en la práctica.
- Entender por qué una alerta de seguridad (aquí, el recambio de agua) debe implementarse como una capa de reglas independiente del modelo predictivo.
- Diseñar una estrategia de contingencia explícita para la pérdida de conexión de un sensor, en vez de asumir que siempre estará disponible.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-SARIMA-8CAAE6)
![MQTT](https://img.shields.io/badge/MQTT-IoT-660066)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-006a87)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del caso](https://fuzzyfrog.ai/es/ai-lab/proyectos/agritech/prediccion-variables-tanque-piscicultura-iot-machine-learning/)
- Referencias citadas arriba en *Enfoque de análisis*
- [`prediccion-variables-tanque-piscicultura-iot-machine-learning.ipynb`](./prediccion-variables-tanque-piscicultura-iot-machine-learning.ipynb)

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `prediccion-variables-tanque-piscicultura-iot-machine-learning.ipynb` en Jupyter, Google Colab o VS Code.
3. Ejecuta todas las celdas en orden; el dataset sintético se genera dentro del propio notebook, no requiere descargas externas.
4. Para probar el pipeline con tu propio sensor, reemplaza la celda de generación de datos por la ingesta real desde tu broker MQTT, manteniendo las columnas `timestamp`, `WaterTemperature`, `Conductivity`, `TDS`, `Ph`, `Amonio`, `Nitrito`, `Nitrato`.
5. Ajusta `UMBRALES_RECAMBIO` y `TOLERANCIA_MAX_LECTURAS` a los valores reales de tu especie y tu infraestructura de sensores antes de usarlo en producción.

---
*Made with ❤️ by FuzzyFrog.AI*
