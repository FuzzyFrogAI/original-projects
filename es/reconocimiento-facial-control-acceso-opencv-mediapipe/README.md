# 🧪 Laboratorio: Control de Acceso con Reconocimiento Facial - ATLAS FuzzyFrog.AI

**Aprende a construir un sistema de control de acceso por reconocimiento facial, desde la detección de rostros en video hasta un umbral de confianza que sabe cuándo rechazar a alguien que el sistema no reconoce.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/reconocimiento-facial-control-acceso-opencv-mediapipe/) | [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
reconocimiento-facial-control-acceso-opencv-mediapipe/
├── reconocimiento-facial-control-acceso-opencv-mediapipe.ipynb   # Notebook consolidado: carga, detección, entrenamiento, evaluación
├── outputs/
│   ├── identidades_sinteticas.csv          # Metadata sintética de las 40 identidades (nombre, cargo)
│   └── bitacora_accesos_sintetica.csv      # Bitácora simulada de eventos de entrada/salida
└── README.md
```

## Enfoque de análisis

- 🧩 **Detección y reconocimiento como funciones separadas.** MediaPipe localiza el rostro dentro del frame; LBPH lo reconoce después, como pasos independientes que se pueden ajustar por separado. Referencia: Viola, P. & Jones, M. (2001). *Rapid Object Detection using a Boosted Cascade of Simple Features*. CVPR.
- 🪶 **LBPH en vez de embeddings profundos.** Con pocas fotos por identidad y sin GPU dedicada, un reconocedor liviano basado en patrones locales rinde mejor que forzar una red profunda sobreajustada. Referencia: Ahonen, T., Hadid, A. & Pietikäinen, M. (2006). *Face Description with Local Binary Patterns: Application to Face Recognition*. IEEE TPAMI.
- 🚧 **Umbral de confianza explícito para "desconocido".** La predicción de LBPH trae una distancia asociada; en vez de usar siempre el match más cercano, se define un umbral que rechaza la identificación cuando la distancia es demasiado alta. Referencia: Grother, P., Ngan, M. & Hanaoka, K. (2019). *Face Recognition Vendor Test (FRVT) Part 2: Identification*. NIST.

## Metas

- Practicar un pipeline completo de reconocimiento facial: detección, extracción, entrenamiento y evaluación.
- Entender por qué el umbral de confianza es una decisión de diseño, no un detalle técnico menor.
- Ver cómo consolidar código disperso en funciones reutilizables que se puedan desplegar.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter)
![OpenCV](https://img.shields.io/badge/OpenCV-contrib-red?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FaceDetection-informational)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-7dce2e)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/reconocimiento-facial-control-acceso-opencv-mediapipe/)
- Papers citados arriba (Viola & Jones, Ahonen et al., Grother et al.)
- Notebook: `reconocimiento-facial-control-acceso-opencv-mediapipe.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Abre `reconocimiento-facial-control-acceso-opencv-mediapipe.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset de rostros (AT&T/Olivetti Faces) se descarga automáticamente.
4. Prueba la función de inferencia con tus propios rostros ajustando `UMBRAL_DESCONOCIDO` a tu cámara.

---

*Made with ❤️ by FuzzyFrog.AI*
