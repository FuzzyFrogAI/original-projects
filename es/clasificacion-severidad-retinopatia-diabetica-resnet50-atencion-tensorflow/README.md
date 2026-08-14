# 🧪 Laboratorio: Clasificación de Severidad de Retinopatía Diabética - FuzzyFrog.AI

**Aprende por qué el accuracy general puede ocultar que un modelo nunca detecta la enfermedad que se supone debe detectar.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-severidad-retinopatia-diabetica-resnet50-atencion-tensorflow/) | [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
clasificacion-severidad-retinopatia-diabetica-resnet50-atencion-tensorflow/
├── clasificacion-severidad-retinopatia-diabetica-resnet50-atencion-tensorflow.ipynb   # Notebook principal: 3 arquitecturas comparadas
├── outputs/                                                                             # Matrices de confusión y reportes generados al correr el notebook
└── README.md                                                                            # Este archivo
```

## Enfoque de análisis

- 🎯 **Category Attention Block + Global Attention Block para desbalance de clases.** Un mapa de atención específico por clase ayuda a capturar detalles visuales distintos entre grados de severidad, en vez de un único mapa compartido. Referencia: He, A., Li, T., Li, N., Wang, K., Fu, H. (2020). *CABNet: Category Attention Block for Imbalanced Diabetic Retinopathy Grading*. IEEE Transactions on Medical Imaging, 40(1), 143-153.
- 🔄 **Transfer learning con fine-tuning en dos fases.** Congelar el backbone al inicio evita destruir los pesos preentrenados con gradientes grandes; descongelar después, con learning rate menor, permite ajuste fino sin perder lo aprendido en ImageNet. Referencia: Yosinski, J. et al. (2014). *How transferable are features in deep neural networks?*. NeurIPS.
- 📊 **Recall por clase como métrica principal, no el accuracy general.** En un dataset desbalanceado, el accuracy general puede ser prácticamente el porcentaje de la clase mayoritaria. Referencia: He, H., Garcia, E.A. (2009). *Learning from Imbalanced Data*. IEEE Transactions on Knowledge and Data Engineering, 21(9), 1263-1284.
- 🏗️ **Comparación controlada de backbones (ResNet50 vs. VGG16) con la misma técnica de atención.** Aislar el backbone como única variable permite atribuir la diferencia de desempeño a esa elección arquitectónica específica. Referencia: He, K. et al. (2016). *Deep Residual Learning for Image Recognition*. CVPR.

## Metas

- Practicar cómo diseñar una comparación justa entre arquitecturas para una tarea de clasificación médica.
- Entender por qué el recall por clase es la métrica que realmente importa en problemas desbalanceados.
- Practicar la implementación de mecanismos de atención (global y por categoría) en Keras funcional.
- Aprender a auditar código heredado en busca de errores silenciosos antes de confiar en un resultado.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-API-D00000?logo=keras&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-severidad-retinopatia-diabetica-resnet50-atencion-tensorflow/)
- Papers de referencia citados arriba (He et al. 2020 CABNet, Yosinski et al. 2014, He & Garcia 2009, He et al. 2016 ResNet)
- Notebook de ejercicios: `clasificacion-severidad-retinopatia-diabetica-resnet50-atencion-tensorflow.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre el notebook: `clasificacion-severidad-retinopatia-diabetica-resnet50-atencion-tensorflow.ipynb`
3. Instala dependencias (`tensorflow`, `scikit-learn`, `scikit-image`, `pandas`, `matplotlib`) y configura tus credenciales de Kaggle para descargar el dataset público `tanlikesmath/diabetic-retinopathy-resized`.
4. Corre las celdas en orden. Las llamadas de entrenamiento están comentadas por defecto (son costosas en tiempo/cómputo); descoméntalas para reproducir el entrenamiento completo.
5. Prueba `construir_modelo()` con `con_atencion=False` o `pesos=None` para replicar tú mismo el experimento de ablación descrito en el artículo.

---
*Este proyecto es un ejercicio técnico/educativo de clasificación de imágenes. No es un dispositivo médico, no está validado clínicamente, y no debe usarse como herramienta de diagnóstico.*

---
*Made with ❤️ by FuzzyFrog.AI*
