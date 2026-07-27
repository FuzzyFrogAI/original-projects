# 🧪 Laboratorio: Generación de Imágenes Sintéticas de Mamografía con GAN - ATLAS FuzzyFrog.AI

**Aprenderás a diseñar una GAN para generar imágenes médicas sintéticas, evaluarlas con métricas que sí se pueden interpretar, y decidir cuándo esos datos sintéticos realmente ayudan a un clasificador downstream.**

🔗 [Plataforma](https://fuzzyfrog.ai/es/) | 📄 [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/gan-imagenes-sinteticas-mamografia-momentos-hu/) | 📁 [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
gan-imagenes-sinteticas-mamografia-momentos-hu/
├── gan-imagenes-sinteticas-mamografia-momentos-hu.ipynb   # Notebook ejecutable: GAN, evaluación y clasificador downstream
├── README.md                                              # Este archivo
└── outputs/                                               # Checkpoints y resultados generados al ejecutar el notebook
```

## Enfoque de análisis

- 🧬 **GAN tipo DCGAN con Conv2DTranspose**, siguiendo la arquitectura convolucional profunda que estabilizó el entrenamiento de GANs para imágenes: Radford, A., Metz, L., & Chintala, S. (2016). *Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks*. [arXiv:1511.06434](https://arxiv.org/abs/1511.06434).
- 📉 **Fréchet Inception Distance (FID)** como métrica estándar de calidad generativa sobre activaciones profundas: Heusel, M., et al. (2017). *GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium*. [arXiv:1706.08500](https://arxiv.org/abs/1706.08500).
- 📐 **Momentos de Hu como métrica morfológica propia**, complementaria a FID/KID, aplicable porque estas imágenes se pueden binarizar con sentido clínico: Hu, M.K. (1962). *Visual Pattern Recognition by Moment Invariants*. IRE Transactions on Information Theory, 8(2), 179-187.
- ⚖️ **Entrenamiento adversarial con discriminador congelado**, base teórica del juego de suma cero entre generador y discriminador: Goodfellow, I., et al. (2014). *Generative Adversarial Networks*. [arXiv:1406.2661](https://arxiv.org/abs/1406.2661).

## Metas

- Diseñar generador y discriminador con arquitecturas convolucionales estables para imágenes médicas.
- Congelar correctamente un submodelo dentro de un modelo combinado en Keras, para evitar que el discriminador se sobre-ajuste durante el entrenamiento adversarial.
- Evaluar calidad generativa combinando métricas no interpretables (FID, KID) con una métrica propia interpretable (momentos de Hu).
- Decidir, con evidencia y no con intuición, cuándo el aumento de datos sintéticos mejora un clasificador y cuándo no.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?logo=tensorflow&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- 🔗 [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- 📄 [Artículo completo con el diagrama del pipeline](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/gan-imagenes-sinteticas-mamografia-momentos-hu/)
- 🗂️ [Dataset público: CBIS-DDSM Breast Cancer Image Dataset (Kaggle)](https://www.kaggle.com/datasets/awsaf49/cbis-ddsm-breast-cancer-image-dataset)
- 📚 Papers citados arriba (Goodfellow 2014, Radford 2016, Heusel 2017, Hu 1962)
- 📓 [`gan-imagenes-sinteticas-mamografia-momentos-hu.ipynb`](./gan-imagenes-sinteticas-mamografia-momentos-hu.ipynb)

## Cómo usar

1. Clona este repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre `gan-imagenes-sinteticas-mamografia-momentos-hu.ipynb` en Jupyter o Google Colab.
3. Descarga el dataset público [CBIS-DDSM desde Kaggle](https://www.kaggle.com/datasets/awsaf49/cbis-ddsm-breast-cancer-image-dataset) y ajusta la ruta `DATASET_PATH` en la celda de carga de datos.
4. Corre el notebook celda por celda: carga de datos → entrenamiento de la GAN → evaluación → clasificador downstream.
5. Prueba la función de generación con tu propio vector de ruido para ver imágenes sintéticas nuevas.

---
*Made with ❤️ by FuzzyFrog.AI*
