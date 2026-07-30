# 🧪 Laboratorio: Detección de Plagas en Algodón con App Móvil - FuzzyFrog.AI

**Objetivo:** aprender a empaquetar una investigación de machine learning ya entrenada dentro de una aplicación móvil real, usando BeeWare, para llevarla de un notebook a una prueba de concepto usable.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/agritech/deteccion-plagas-algodon-app-movil-beeware-mlp/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
deteccion-plagas-algodon-app-movil-beeware-mlp/
├── deteccion-plagas-algodon-app-movil-beeware-mlp.ipynb   # Notebook: extracción de características, MLP, evaluación y guardado del modelo
├── app.py                                                  # App móvil (BeeWare / Toga): cámara, subida de imagen, consulta de resultado
├── pyproject.toml                                          # Configuración de Briefcase/BeeWare para empaquetar la app
├── outputs/
│   └── dataset_sintetico_caracteristicas_algodon.csv       # Dataset sintético de vectores de características
└── README.md                                                # Este archivo
```

## Enfoque de análisis

- 🖼️ **Extracción de características antes de clasificar:** cada imagen se convierte a escala de grises, se redimensiona, se normaliza y se concatena con su histograma de intensidades, en vez de alimentar el modelo con píxeles crudos.
- 🧠 **Perceptrón multicapa como modelo base:** un modelo más simple que una red convolucional profunda, adecuado para validar la viabilidad de la prueba de concepto antes de invertir en arquitecturas más pesadas.
- 📱 **Interfaz nativa con un solo código Python:** BeeWare y Toga permiten construir una app instalable con acceso real a la cámara del dispositivo, sin salir del mismo lenguaje usado para entrenar el modelo.
- 📋 **Documentación honesta de un ajuste de datos:** filtrar ejemplos mal clasificados del entrenamiento mejora las métricas medidas, pero se documenta como una decisión que merece más análisis antes de escalar a producción.

Referencia pública sobre el tipo de datos e imágenes de plagas y enfermedades de algodón: Li, R., He, Y., Li, Y., Qin, W., Abbas, A., Ji, R., et al. (2024). Identification of cotton pest and disease based on CFNet-VoV-GCSP-LSKNet-YOLOv8s: a new era of precision agriculture. Frontiers in Plant Science, 15, 1348402.

## Metas

- Extraer características de imágenes para tareas de clasificación sin usar una red convolucional profunda.
- Entrenar, evaluar y refinar un modelo de clasificación multicategoría.
- Empaquetar un modelo de machine learning dentro de una app móvil real con BeeWare.
- Reconocer los límites de una arquitectura de prueba de concepto frente a una de producción.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-blue)
![BeeWare](https://img.shields.io/badge/BeeWare-Toga-orange)
![scikit--learn](https://img.shields.io/badge/scikit--learn-MLP-yellow)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/agritech/deteccion-plagas-algodon-app-movil-beeware-mlp/)
- Referencia citada en "Enfoque de análisis" (ver arriba)
- Notebook: `deteccion-plagas-algodon-app-movil-beeware-mlp.ipynb`
- App: `app.py` + `pyproject.toml`

## Cómo usar

1. Clona este repositorio.
2. Para el notebook: ábrelo en Jupyter o Google Colab y corre las celdas en orden, el dataset sintético se carga automáticamente desde `outputs/`.
3. Para la app: instala BeeWare (`pip install briefcase`), configura las variables de entorno indicadas en `app.py` (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`, `MONGODB_URI`) y corre `briefcase dev` para probarla localmente.
4. Antes de empaquetar para Android o iOS, revisa `pyproject.toml` y ajusta el `bundle` y los identificadores según tu propio proyecto.

**Importante:** nunca escribas credenciales reales directamente en `app.py` ni en `pyproject.toml`. Usa variables de entorno o un archivo `.env` fuera del control de versiones.

---

*Made with ❤️ by FuzzyFrog.AI*
