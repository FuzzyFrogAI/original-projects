# 🧪 Laboratorio: Predicción de Venta de Boletos por Punto de Venta - ATLAS FuzzyFrog.AI

**Aprende por qué la codificación de una variable categórica puede importar más que la elección del modelo, y por qué esa decisión depende de entender el negocio, no solo de preguntarle a un modelo de lenguaje.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-venta-boletos-puntos-venta-codificacion-ordinal/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
prediccion-venta-boletos-puntos-venta-codificacion-ordinal/
├── prediccion-venta-boletos-puntos-venta-codificacion-ordinal.ipynb   # Notebook principal: codificación, comparación de modelos
├── outputs/
│   └── venta_boletos_sintetico.csv   # Dataset sintético: eventos, zonas, precio y venta
└── README.md                          # Este archivo
```

## Enfoque de análisis

- 🎯 **Replantear el problema como tabular, no como serie de tiempo.** Tener fechas no implica continuidad temporal densa; el objetivo real era predecir eventos futuros con características propias. Referencia: Elsayed, S., Thyssens, D., Rashed, A., Jomaa, H. S., & Schmidt-Thieme, L. (2021). *Do We Really Need Deep Learning Models for Time Series Forecasting?*. https://arxiv.org/abs/2101.02118

- 🔢 **Codificación ordinal por popularidad, no one-hot, para la variable de mayor cardinalidad.** Con un dataset pequeño, expandir una categórica en columnas binarias diluye la señal y multiplica dimensiones; una codificación ordinal basada en un criterio de negocio real (volumen histórico de ventas) comprime esa señal en una sola variable. Referencia: Potdar, K., Pardawala, T. S., & Pai, C. D. (2017). *A Comparative Study of Categorical Variable Encoding Techniques for Neural Network Classifiers*. International Journal of Computer Applications, 175(4). https://doi.org/10.5120/ijca2017915495

- 🔄 **Codificación cíclica seno-coseno para variables de calendario.** Día y mes son cíclicos, no lineales; esta transformación evita que el modelo trate el 31 de diciembre y el 1 de enero como fechas lejanas. Referencia: *An Experimental Assessment of Treatments for Cyclical Data*. https://scholarworks.calstate.edu/downloads/pv63g5147

- 🌲 **Comparar familias de modelos completas, no ajustar una sola.** Árboles, ensambles, una LSTM y modelos clásicos de series de tiempo se evaluaron con la misma métrica (MAPE), confirmando que un ensamble de árboles se ajustaba mejor a este problema tabular y pequeño que la alternativa de deep learning o series de tiempo.

## Metas

- Practicar la diferencia entre codificación ordinal, one-hot y cíclica, y cuándo usar cada una
- Entender por qué el contexto de negocio, no solo la forma de los datos, determina la mejor decisión de ingeniería de características
- Comparar múltiples familias de modelos de regresión con una métrica de error consistente (MAPE)
- Reconocer las limitaciones de un dataset pequeño, incluso cuando las métricas de prueba se ven bien

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-scikit--learn%20%7C%20XGBoost-F7931E)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + discusión sobre el rol del LLM en las decisiones de diseño): https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-venta-boletos-puntos-venta-codificacion-ordinal/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `prediccion-venta-boletos-puntos-venta-codificacion-ordinal.ipynb` y `outputs/venta_boletos_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `prediccion-venta-boletos-puntos-venta-codificacion-ordinal.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/venta_boletos_sintetico.csv`.
4. Para probar el pipeline con tu propio dataset, respeta las mismas columnas (`Evento`, `dia`, `mes`, `anio`, `Zona`, `Precio`, `Venta`) y vuelve a correr desde la sección de modelado; el ranking de eventos y las codificaciones se recalculan automáticamente.

---

*Made with ❤️ by FuzzyFrog.AI*
