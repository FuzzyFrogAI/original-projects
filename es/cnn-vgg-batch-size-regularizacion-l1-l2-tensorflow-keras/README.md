# 🧪 Laboratorio: CNN tipo VGG — Batch Size, Dataset y Regularización L1/L2 - FuzzyFrog.AI

**Aprende a medir el efecto real de un hiperparámetro, aislando una sola variable a la vez, en vez de asumir cuál es "el mejor".**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/cnn-vgg-batch-size-regularizacion-l1-l2-tensorflow-keras/) | [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
cnn-vgg-batch-size-regularizacion-l1-l2-tensorflow-keras/
├── cnn-vgg-batch-size-regularizacion-l1-l2-tensorflow-keras.ipynb   # Notebook principal: arquitectura, 3 barridos de hiperparámetros y hallazgos
├── outputs/                                                          # Figuras generadas al correr el notebook
└── README.md                                                         # Este archivo
```

## Enfoque de análisis

- 🧱 **Arquitectura base fija, un solo hiperparámetro variable por experimento.** Aislar la variable es lo que permite atribuir cualquier cambio de comportamiento a una sola causa. Referencia: Goodfellow, I., Bengio, Y., Courville, A. (2016). *Deep Learning*, cap. 8 (Optimización para entrenar modelos profundos). MIT Press.
- ⏱️ **Medir siempre tiempo de cómputo junto con accuracy/loss.** La calidad de un modelo no es el único criterio de decisión en un proyecto real; el costo de entrenarlo también importa. Referencia: Masters, D., Luschi, C. (2018). *Revisiting Small Batch Training for Deep Neural Networks*. arXiv:1804.07612.
- 📉 **Leer la dinámica completa de las curvas, no solo la métrica final.** El punto donde divergen train y validación es más informativo que cualquier número aislado al final del entrenamiento. Referencia: Ying, X. (2019). *An Overview of Overfitting and its Solutions*. Journal of Physics: Conference Series.
- 🎛️ **Regularización como perilla continua, no como interruptor.** Barrer varios órdenes de magnitud de lambda revela el rango donde la técnica realmente ayuda. Referencia: Cortes, C., Mohri, M., Rostamizadeh, A. (2012). *L2 Regularization for Learning Kernels*. arXiv:1205.2653.

## Metas

- Practicar cómo leer `model.summary()` y calcular manualmente los parámetros entrenables de una CNN.
- Entender el trade-off real entre batch size, tiempo de cómputo y generalización.
- Practicar el diseño de un experimento de barrido de hiperparámetros con código reutilizable, en vez de copiar y pegar bloques casi idénticos.
- Aprender a diagnosticar sobreajuste a partir de las curvas de entrenamiento y validación, no solo del accuracy final.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-API-D00000?logo=keras&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/cnn-vgg-batch-size-regularizacion-l1-l2-tensorflow-keras/)
- Papers de referencia citados arriba (Goodfellow et al. 2016, Masters & Luschi 2018, Ying 2019, Cortes et al. 2012)
- Notebook de ejercicios: `cnn-vgg-batch-size-regularizacion-l1-l2-tensorflow-keras.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre el notebook: `cnn-vgg-batch-size-regularizacion-l1-l2-tensorflow-keras.ipynb`
3. Instala dependencias (`tensorflow`, `scikit-learn`, `matplotlib`, `pandas`) y corre las celdas en orden. CIFAR-10 se descarga automáticamente vía `tensorflow.keras.datasets`.
4. Modifica la lista `batch_sizes`, `tamanios` o `configs_reg` para probar tus propios valores usando la misma función `construir_y_entrenar()`.
5. Extiende el experimento agregando `Dropout`, `BatchNormalization` o `ImageDataGenerator` (data augmentation) a la función base, siguiendo la misma disciplina de aislar una variable a la vez.

---
*Made with ❤️ by FuzzyFrog.AI*
