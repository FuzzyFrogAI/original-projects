# 🧪 Laboratorio: Clasificación de Leucemia Linfoblástica Aguda con CNN + GAN - FuzzyFrog.AI

**Aprende a usar una GAN para generar datos sintéticos por clase cuando un dataset médico está desbalanceado, y a verificar que ningún resultado de accuracy esconda una fuga de datos.**

⚠️ **Nota importante:** este proyecto es una herramienta educativa y de investigación. No es un dispositivo de diagnóstico clínico y ninguna predicción de este pipeline debe usarse para decisiones médicas reales.

🔗 Enlaces rápidos: [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-leucemia-linfoblastica-cnn-gan/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```plaintext
clasificacion-leucemia-linfoblastica-cnn-gan/
├── README.md                                          ← este archivo
├── clasificacion-leucemia-linfoblastica-cnn-gan.ipynb  ← notebook completo, ejecutable en Colab
└── dataset/
    ├── muestra_benign.jpg                              ← imagen de muestra, clase Benign
    ├── muestra_early.jpg                                ← imagen de muestra, clase Early
    ├── muestra_pre.jpg                                  ← imagen de muestra, clase Pre
    └── muestra_pro.jpg                                  ← imagen de muestra, clase Pro
```

**Dataset completo:** [Acute Lymphoblastic Leukemia (ALL) image dataset](https://www.kaggle.com/datasets/mehradaria/leukemia), Aria et al. 2021, DOI: 10.34740/KAGGLE/DSV/2175623. Descargar y montar en Google Drive para reproducir resultados con las 3,256 imágenes completas.

## Enfoque de análisis

- 🧬 **GAN por clase para data augmentation morfológica.** En vez de solo rotar o voltear imágenes, se entrena un generador/discriminador por clase para sintetizar variabilidad celular nueva, priorizando la clase con menos ejemplos reales. Referencia: [Goodfellow, I. et al. (2014). *Generative Adversarial Networks*.](https://arxiv.org/abs/1406.2661)
- ⚖️ **Baseline simple antes que arquitectura compleja.** Se usa una CNN vanilla de 2 capas como punto de partida explícito, dejando el transfer learning como extensión medible, no como default. Referencia: [Ghaderzadeh, M. et al. (2022). *A fast and efficient CNN model for B-ALL diagnosis and its subtypes classification using peripheral blood smear images*.](https://onlinelibrary.wiley.com/doi/10.1002/int.22753)
- 🔍 **Verificación de fuga de datos (data leakage).** Cualquier accuracy reportado se contrasta primero contra la pregunta: ¿train y test comparten alguna imagen fuente? Un 100% de accuracy sin responder eso no es una métrica confiable.

## Metas

- Practicar el diseño de una GAN condicionada por clase para data augmentation en datasets médicos pequeños.
- Aprender a verificar formas de salida entre bloques de una arquitectura antes de asumir que compila correctamente.
- Entender por qué el desbalance de clases en salud no siempre se resuelve solo con reponderación de la pérdida.
- Practicar la detección de fuga de datos en pipelines de clasificación de imágenes.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Preprocesamiento-5C3EE8?logo=opencv&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter%2FColab-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-leucemia-linfoblastica-cnn-gan/)
- Papers citados en Enfoque de análisis (ver arriba)
- Notebook: `clasificacion-leucemia-linfoblastica-cnn-gan.ipynb`
- Dataset completo: [Kaggle — Acute Lymphoblastic Leukemia (ALL) image dataset](https://www.kaggle.com/datasets/mehradaria/leukemia)

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Abre `clasificacion-leucemia-linfoblastica-cnn-gan.ipynb` en Google Colab o Jupyter.
3. Para una prueba rápida del pipeline, corre las celdas en orden tal cual vienen — usan las 4 imágenes de muestra en `dataset/`.
4. Para resultados reales, descarga el dataset completo de Kaggle, móntalo en Drive, y descomenta las celdas marcadas con `# Descomentar para correr con el dataset completo`.

---

*Made with ❤️ by FuzzyFrog.AI*
