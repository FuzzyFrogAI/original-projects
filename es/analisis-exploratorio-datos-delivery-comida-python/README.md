# 🧪 Laboratorio: Detección de Uso de Casco de Seguridad con YOLOv5 - FuzzyFrog.AI

**Aprende por qué remover una clase mal representada puede mejorar el desempeño general de un modelo de detección de objetos más que cualquier ajuste de hiperparámetros.**

⚠️ **Nota de seguridad:** este notebook usa una variable de entorno para la API key de Roboflow. Nunca escribas una API key directamente en el código ni la subas a un repositorio.

🔗 Enlaces rápidos: [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/deteccion-uso-casco-seguridad-yolov5/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```plaintext
deteccion-uso-casco-seguridad-yolov5/
├── README.md                                          ← este archivo
├── deteccion-uso-casco-seguridad-yolov5.ipynb          ← notebook completo, ejecutable en Colab
└── dataset/
    ├── muestra_casco_1.jpg                             ← imagen sintetica de muestra + etiqueta YOLO
    ├── muestra_casco_1.txt
    ├── muestra_casco_2.jpg
    └── muestra_casco_2.txt
```

**Dataset completo:** dataset público de detección de cascos de seguridad, disponible en Roboflow Universe. Requiere una API key propia de Roboflow (gratuita) para descargar — nunca la de otra persona ni una key expuesta en un tutorial.

## Enfoque de análisis

- ⚖️ **Balance de clases antes que ajuste de hiperparámetros.** Se revisó el conteo de instancias por clase antes de entrenar, y se removió la clase "persona" por estar muy subrepresentada, en vez de intentar compensarla con sobremuestreo o ajuste fino. Referencia: [He, H. & Garcia, E.A. (2009). *Learning from Imbalanced Data*. IEEE TKDE.](https://ieeexplore.ieee.org/document/5128907)
- 🎯 **Transfer learning para datasets pequeños.** Se parte de pesos preentrenados en COCO (`yolov5s.pt`) en vez de entrenar desde cero, porque el dataset de cascos es pequeño para una arquitectura de este tamaño. Referencia: [Jocher, G. et al. (2022). *YOLOv5 by Ultralytics*.](https://github.com/ultralytics/yolov5)
- 🔐 **Manejo seguro de credenciales.** La API key de Roboflow se lee desde una variable de entorno, con una validación explícita que detiene la ejecución si no está definida, en vez de fallar de forma confusa más adelante.

## Metas

- Practicar el diagnóstico de balance de clases antes de entrenar un modelo de detección de objetos.
- Aprender a aplicar transfer learning con YOLOv5 sobre un dataset pequeño y específico.
- Entender por qué el mAP promedio puede esconder el mal desempeño de una sola clase.
- Practicar el manejo correcto de credenciales (API keys) en notebooks compartidos.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![YOLOv5](https://img.shields.io/badge/YOLOv5-Deteccion%20de%20objetos-00FFFF?logo=pytorch&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-Transfer%20Learning-EE4C2C?logo=pytorch&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter%2FColab-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/deteccion-uso-casco-seguridad-yolov5/)
- Referencias citadas en Enfoque de análisis (ver arriba)
- Notebook: `deteccion-uso-casco-seguridad-yolov5.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Abre `deteccion-uso-casco-seguridad-yolov5.ipynb` en Google Colab (necesitas GPU para entrenar en tiempo razonable).
3. Crea tu propia API key gratuita en Roboflow y defínela como variable de entorno — nunca la escribas directamente en el notebook.
4. Corre las celdas en orden. La celda de entrenamiento incluye una prueba de humo con un dataset sintético pequeño para validar que el pipeline funciona antes de correr el entrenamiento completo.

---

*Made with ❤️ by FuzzyFrog.AI*
