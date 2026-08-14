# 🧪 Laboratorio: Clasificación de Variedades de Arroz - FuzzyFrog.AI

**Aprende el flujo de 4 pasos para convertir un notebook de clasificación en una contribución comparable con la literatura.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/agritech/clasificacion-variedades-arroz-cnn-xception-benchmark-articulo-conferencia/) | [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
clasificacion-variedades-arroz-cnn-xception-benchmark-articulo-conferencia/
├── clasificacion-variedades-arroz-cnn-xception-benchmark-articulo-conferencia.ipynb   # Notebook principal: CNN simple vs. Xception, comparado contra la referencia
├── outputs/                                                                             # Matrices de confusión y gráficas generadas al correr el notebook
└── README.md                                                                            # Este archivo
```

## Enfoque de análisis

- 📚 **Usar el artículo de origen del dataset como referencia, no un paper cualquiera.** Cuando el propio dataset cita su artículo de origen, es el punto de comparación más justo posible: mismos datos, mismas clases. Referencia: Koklu, M., Cinar, I., Taspinar, Y.S. (2021). *Classification of rice varieties with deep learning methods*. Computers and Electronics in Agriculture, 187, 106285.
- ⚖️ **Comparar arquitecturas de complejidad distinta bajo las mismas condiciones.** Aislar CNN simple vs. Xception con transfer learning, sobre el mismo dataset y evaluación, permite atribuir la diferencia de desempeño a la arquitectura, no a variables externas. Referencia: Yosinski, J. et al. (2014). *How transferable are features in deep neural networks?*. NeurIPS.
- 🔍 **Un resultado contraintuitivo bien argumentado es una contribución válida.** No siempre "mejorar la métrica" es el aporte; entender y explicar por qué un enfoque más sofisticado rindió peor también lo es. Referencia: Raghu, M. et al. (2019). *Transfusion: Understanding Transfer Learning for Medical Imaging*. NeurIPS (discute cuándo transfer learning desde ImageNet no aporta el beneficio esperado en dominios visualmente distintos).
- 📝 **Mapear resultados a la estructura estándar de un artículo científico.** Título, abstract, introducción, fundamentos, metodología, resultados, conclusiones: cada sección responde una pregunta específica del lector. Referencia: Fricke, S. (2019). *IMRAD structure and how to write a research paper*. Journal of the Medical Library Association.

## Metas

- Practicar cómo encontrar el mejor artículo de referencia para un dataset dado.
- Aprender a diseñar una comparación justa entre un modelo simple y uno con transfer learning.
- Practicar cómo leer e interpretar un resultado contraintuitivo sin forzar una lectura favorable.
- Entender qué lleva cada sección de un artículo de conferencia y cómo mapear tu propio proyecto a esa estructura.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-API-D00000?logo=keras&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/agritech/clasificacion-variedades-arroz-cnn-xception-benchmark-articulo-conferencia/)
- [Rice Image Dataset (Kaggle)](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset) — URL verificada y vigente
- [Artículo de referencia (Koklu et al., 2021)](https://doi.org/10.1016/j.compag.2021.106285)
- Notebook de ejercicios: `clasificacion-variedades-arroz-cnn-xception-benchmark-articulo-conferencia.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre el notebook: `clasificacion-variedades-arroz-cnn-xception-benchmark-articulo-conferencia.ipynb`
3. Instala dependencias (`tensorflow`, `scikit-learn`, `opencv-python`, `imutils`, `seaborn`) y configura tus credenciales de Kaggle para descargar el dataset público `muratkokludataset/rice-image-dataset`.
4. Corre las celdas en orden. Reproduce la comparación CNN simple vs. Xception, y contrástala contra el 100% reportado por el artículo de referencia.
5. Extiende el flujo a tu propio producto agrícola: busca el paper de origen de tu dataset, registra su métrica principal, ejecuta tu experimento, y compara.

---
*Made with ❤️ by FuzzyFrog.AI*
