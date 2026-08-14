# 🧪 Laboratorio: Enriquecimiento Cross-Domain con Embeddings de Comportamiento - FuzzyFrog.AI

**Aquí no aprendes a subir un accuracy, aprendes a desconfiar de uno perfecto y a diseñar el experimento que confirma si tu técnica realmente generaliza.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/ciberseguridad/enriquecimiento-cross-domain-embeddings-conductuales-deteccion-anomalias-red/) | [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
enriquecimiento-cross-domain-embeddings-conductuales-deteccion-anomalias-red/
├── enriquecimiento-cross-domain-embeddings-conductuales-deteccion-anomalias-red.ipynb  # Notebook principal: perfilamiento, enriquecimiento y clasificación
├── dataset_sintetico_perfiles_comportamiento.csv                                       # Dataset sintético de comportamiento (90 usuarios, demostrativo)
├── outputs/                                                                             # Figuras y artefactos generados al correr el notebook
└── README.md                                                                            # Este archivo
```

## Enfoque de análisis

- 🧩 **Autoencoder + clustering jerárquico para perfilamiento conductual.** Reducir a un espacio latente antes de agrupar mejora sustancialmente la separación de clusters frente al clustering directo sobre datos crudos. Referencia: Ikotun, A.M. et al. (2023). *K-means clustering algorithms: A comprehensive review, variants analysis, and advances in the era of big data*. Information Sciences.
- ⚔️ **Autoencoders adversariales para alineación cross-domain.** Un discriminador que distingue el dominio de origen de cada embedding, combinado con la pérdida de reconstrucción, fuerza a que dos espacios de datos sin correspondencia etiquetada compartan geometría. Referencia: Ganin, Y. et al. (2016). *Domain-Adversarial Training of Neural Networks*. Journal of Machine Learning Research.
- 🎯 **Emparejamiento por similitud coseno instancia a instancia.** En vez de un enriquecimiento global (mismo contexto para todos los registros), cada instancia recibe el contexto más relevante disponible, preservando variabilidad real. Referencia: Xia, P. et al. (2015). *Learning similarity with cosine similarity ensemble*. Information Sciences.
- 📉 **Ablación con interpretación de dinámica de entrenamiento, no solo de métrica final.** Comparar la misma arquitectura con y sin la técnica propuesta, y leer la brecha train/validación como señal de generalización, no solo el accuracy. Referencia: Ying, X. (2019). *An Overview of Overfitting and its Solutions*. Journal of Physics: Conference Series.

## Metas

- Practicar cómo alinear dos dominios de datos heterogéneos sin correspondencia etiquetada entre registros.
- Aprender a diseñar un experimento de ablación honesto para validar si una técnica de enriquecimiento realmente aporta generalización.
- Entender por qué un accuracy perfecto en un problema de seguridad es una señal de alerta, no de éxito.
- Practicar validación cruzada estratificada como mecanismo de confianza sobre un resultado, más allá de un solo split.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.8-EE4C2C?logo=pytorch&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/ciberseguridad/enriquecimiento-cross-domain-embeddings-conductuales-deteccion-anomalias-red/)
- Papers de referencia citados arriba (Ikotun et al. 2023, Ganin et al. 2016, Xia et al. 2015, Ying 2019)
- Notebook de ejercicios: `enriquecimiento-cross-domain-embeddings-conductuales-deteccion-anomalias-red.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre el notebook: `enriquecimiento-cross-domain-embeddings-conductuales-deteccion-anomalias-red.ipynb`
3. Instala dependencias (`pandas`, `numpy`, `torch`, `scikit-learn`, `matplotlib`) y corre las celdas en orden.
4. Descarga tu propia copia del dataset UNSW-NB15 y ajusta la ruta `RUTA_UNSW` en la celda de carga de datos.
5. Prueba la función de emparejamiento por similitud coseno con tus propios embeddings para ver cómo cambia el dataset enriquecido.

---
*Made with ❤️ by FuzzyFrog.AI*
