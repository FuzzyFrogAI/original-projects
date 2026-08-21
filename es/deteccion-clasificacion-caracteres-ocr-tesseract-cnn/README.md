# 🧪 Laboratorio: Detección y Clasificación de Caracteres en Documentos - FuzzyFrog.AI

**Aprende a combinar un motor de OCR clásico con un clasificador de caracteres propio para extraer texto de documentos de calidad variable, y a decidir cuándo el preprocesamiento de imagen importa más que el modelo.**

🔗 Enlaces rápidos: [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/gobierno/deteccion-clasificacion-caracteres-ocr-tesseract-cnn/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```plaintext
deteccion-clasificacion-caracteres-ocr-tesseract-cnn/
├── README.md                                          ← este archivo
├── deteccion-clasificacion-caracteres-ocr-tesseract-cnn.ipynb   ← notebook completo, ejecutable en Colab
└── dataset/
    ├── caracteres_fuentes_sintetico.csv                ← dataset sintético de caracteres por fuente (20x20 px)
    ├── comparacion_modelos.csv                         ← tabla de resultados: baseline vs CNN
    ├── ine_muestra_1.png                                ← espécimen de muestra público
    └── ine_muestra_2.png                                ← espécimen de muestra público
```

## Enfoque de análisis

- 🖼️ **Preprocesamiento antes que ajuste de modelo.** Se prioriza corregir la imagen de entrada (upscaling, binarización) antes de tocar cualquier parámetro del motor de OCR o del clasificador, porque la calidad de imagen resultó ser la variable de mayor impacto en el resultado final. Referencia: [Smith, R. (2007). *An Overview of the Tesseract OCR Engine*. ICDAR.](https://ieeexplore.ieee.org/document/4376991)
- 🔤 **Dataset sintético de caracteres por fuente.** En vez de depender de un dataset propietario etiquetado, se generan caracteres renderizados en distintas tipografías con variación de tamaño, posición y ruido — controlando exactamente la variabilidad que aprende el modelo. Referencia: [Jaderberg, M. et al. (2014). *Synthetic Data and Artificial Neural Networks for Natural Scene Text Recognition*.](https://arxiv.org/abs/1406.2227)
- 🧠 **Baseline antes de arquitectura compleja.** Se entrena primero una regresión logística sobre los píxeles crudos, y solo se justifica la CNN si supera ese baseline con un margen claro y medible.

## Metas

- Practicar la construcción de un pipeline de OCR de dos etapas: detección clásica + clasificación por deep learning.
- Aprender a diagnosticar problemas de calidad de imagen antes de ajustar hiperparámetros de modelo.
- Practicar la generación de datasets sintéticos como alternativa cuando no hay datos reales etiquetados disponibles.
- Entender cómo comparar un baseline simple contra un modelo más complejo con criterio, no por default.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-CNN-EE4C2C?logo=pytorch&logoColor=white)
![Tesseract](https://img.shields.io/badge/OCR-Tesseract-5C2D91)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter%2FColab-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/gobierno/deteccion-clasificacion-caracteres-ocr-tesseract-cnn/)
- Papers citados en Enfoque de análisis (ver arriba)
- Notebook: `deteccion-clasificacion-caracteres-ocr-tesseract-cnn.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Abre `deteccion-clasificacion-caracteres-ocr-tesseract-cnn.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden — la primera celda instala Tesseract y las dependencias de Python.
4. Al final del notebook puedes cargar `dataset/char_cnn.pt` con el modelo ya entrenado y probar la función de clasificación sobre un carácter nuevo recortado de una imagen propia.

---

*Made with ❤️ by FuzzyFrog.AI*
