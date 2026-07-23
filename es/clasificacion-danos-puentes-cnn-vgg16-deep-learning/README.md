# 🧪 Laboratorio: Clasificación de Daños en Puentes con CNN (VGG16) - ATLAS FuzzyFrog.AI

**Aprende a construir un clasificador de daños estructurales en puentes con transfer learning, usando datos abiertos, y a documentar honestamente cuando un primer experimento no sale bien.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/clasificacion-danos-puentes-cnn-vgg16-deep-learning/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
clasificacion-danos-puentes-cnn-vgg16-deep-learning/
├── clasificacion-danos-puentes-cnn-vgg16-deep-learning.ipynb   # Notebook: carga, VGG16, 2 experimentos y evaluación
├── data/
│   └── imagenes_puentes/   # Estructura ImageFolder de ejemplo, sustituir por datos propios o abiertos
└── README.md
```

## Enfoque de análisis

- 🖼️ **Transfer learning con VGG16 y capas convolucionales congeladas**, en vez de entrenar una CNN desde cero. Referencia: Simonyan, K., & Zisserman, A. (2014). Very Deep Convolutional Networks for Large-Scale Image Recognition. *arXiv preprint arXiv:1409.1556*.
- 📂 **Datos abiertos reales de inspección de puentes**, en vez de esperar a tener un dataset propio. Referencia: Flotzinger, J., Rösch, P. J., Oswald, N., & Braml, T. (2023). dacl1k: Real-World Bridge Damage Dataset Putting Open-Source Data to the Test. *arXiv preprint arXiv:2309.03763*.
- 🔍 **Machine learning en monitoreo de salud estructural, marco general del problema.** Referencia: Flah, M., Nunez, I., Ben Chaabene, W., & Nehdi, M. L. (2021). Machine learning algorithms in civil structural health monitoring: a systematic review. *Archives of Computational Methods in Engineering, 28*(4), 2621-2643.
- ⚠️ **Un resultado pobre documentado como hallazgo, no escondido**, lo que llevó a refinar el conjunto de clases. Referencia: Malekloo, A., Ozer, E., AlHamaydeh, M., & Girolami, M. (2022). Machine learning and structural health monitoring overview with emerging technology and high-dimensional data source highlights. *Structural Health Monitoring, 21*(4), 1906-1955.

## Metas

- Practicar transfer learning con una arquitectura CNN clásica (VGG16) sobre un problema de clasificación de imágenes con pocos datos.
- Aprender a evaluar con matriz de confusión y reporte de clasificación por clase, no solo con el accuracy general.
- Ver un ejemplo real de por qué reportar un resultado pobre, entendiendo su causa, es parte de la contribución de un proyecto, no un defecto que se oculta.
- Practicar qué hacer cuando un proyecto necesita datos que no existen todavía: cómo buscar y evaluar datos abiertos relevantes.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-VGG16%20Transfer%20Learning-EE4C2C?logo=pytorch&logoColor=white)
![torchvision](https://img.shields.io/badge/torchvision-ImageFolder-EE4C2C?logo=pytorch&logoColor=white)
![Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/clasificacion-danos-puentes-cnn-vgg16-deep-learning/)
- Papers citados en "Enfoque de análisis" arriba
- `clasificacion-danos-puentes-cnn-vgg16-deep-learning.ipynb` (notebook principal)

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Descarga el dataset dacl1k y/o el building-inspection-toolkit (ligas en las referencias) y organiza las imágenes en `data/imagenes_puentes/` con una subcarpeta por clase.
3. Abre `clasificacion-danos-puentes-cnn-vgg16-deep-learning.ipynb` en Jupyter o Google Colab.
4. Corre las celdas en orden: carga de datos → modelo VGG16 → experimento 1 (conjunto amplio) → evaluación → experimento 2 (conjunto refinado) → evaluación con imágenes nuevas.
5. Para probar con tu propio conjunto de clases, ajusta la lista `clases_refinadas` según qué categorías de daño tengan suficiente cantidad y calidad de imágenes en tus datos.

---
*Made with ❤️ by FuzzyFrog.AI*
