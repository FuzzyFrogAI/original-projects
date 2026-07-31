# 🧪 Laboratorio: Detección de Violencia en Video de Vigilancia - ATLAS FuzzyFrog.AI

**Aprende a reutilizar un modelo de pose ya entrenado, convertir sus keypoints en features de movimiento, y validar cada paso extra del pipeline con un estudio de ablación en vez de intuición.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/seguridad/deteccion-violencia-video-vigilancia-pose-estimation-gru/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
deteccion-violencia-video-vigilancia-pose-estimation-gru/
├── deteccion-violencia-video-vigilancia-pose-estimation-gru.ipynb   # Notebook principal: features de movimiento, ablación, GRU
├── outputs/
│   └── features_movimiento_sintetico.csv   # Dataset sintético: features por persona/segmento + etiqueta Normal/Violent
└── README.md                                # Este archivo
```

## Enfoque de análisis

- 🕺 **Reutilizar un modelo de pose ya entrenado, sin reentrenarlo.** La detección de personas y sus keypoints se resuelve con un modelo de pose existente; el esfuerzo propio se concentra después de ese punto. Referencia: Cao, Z., Simon, T., Wei, S. E., & Sheikh, Y. (2017). *Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields*. https://arxiv.org/abs/1611.08050

- 🏃 **Velocidad y aceleración del movimiento como features, no el video crudo.** Un cambio brusco en el flujo de movimiento entre frames es más informativo que la imagen completa para detectar un golpe o forcejeo. Referencia: Simonyan, K., & Zisserman, A. (2014). *Two-Stream Convolutional Networks for Action Recognition in Videos*. https://arxiv.org/abs/1406.2199

- 🎯 **Filtro de Kalman para suavizar la serie de ángulos.** Se valida con un estudio de ablación (con y sin filtro) antes de dejarlo fijo en el pipeline. Referencia: Kalman, R. E. (1960). *A New Approach to Linear Filtering and Prediction Problems*. Journal of Basic Engineering, 82(1), 35–45. https://doi.org/10.1115/1.3662552

- 🔍 **Ajuste de hiperparámetros con búsqueda bayesiana (Optuna).** En vez de quedarse con la primera configuración razonable del GRU, se corre una búsqueda bayesiana combinada con validación cruzada. Referencia: Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). *Optuna: A Next-generation Hyperparameter Optimization Framework*. https://arxiv.org/abs/1907.10902

## Metas

- Practicar la construcción de features de movimiento (velocidad, aceleración, energía) a partir de datos de pose
- Diseñar y correr un estudio de ablación honesto, comparando dos variantes del mismo modelo
- Entrenar un clasificador GRU binario y evaluarlo con AUC, matriz de confusión y reporte de clasificación
- Entender cuándo conviene reutilizar un modelo pre-entrenado en vez de entrenar uno propio desde cero

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-TensorFlow%2FKeras-FF6F00)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo del pipeline): https://fuzzyfrog.ai/es/ai-lab/proyectos/seguridad/deteccion-violencia-video-vigilancia-pose-estimation-gru/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `deteccion-violencia-video-vigilancia-pose-estimation-gru.ipynb` y `outputs/features_movimiento_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `deteccion-violencia-video-vigilancia-pose-estimation-gru.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/features_movimiento_sintetico.csv`.
4. Para probar el clasificador entrenado sobre nuevas features, reemplaza la celda de carga de datos por tu propia tabla de features (mismas columnas) y vuelve a correr desde la sección de modelado.

---

*Made with ❤️ by FuzzyFrog.AI*
