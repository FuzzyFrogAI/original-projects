# 🧪 Laboratorio: Clasificación de Riesgo de Salud Mental con NLP y Embeddings - ATLAS FuzzyFrog.AI

**Aprenderás a diseñar un clasificador de texto para priorizar canalización a salud mental, eligiendo un modelo lo bastante moderno para ser bueno y lo bastante ligero para caber en una arquitectura serverless de bajo costo.**

🔗 [Plataforma](https://fuzzyfrog.ai/es/) | 📄 [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-riesgo-salud-mental-nlp-embeddings/) | 📁 [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
clasificacion-riesgo-salud-mental-nlp-embeddings/
├── clasificacion-riesgo-salud-mental-nlp-embeddings.ipynb   # Notebook ejecutable: embeddings, clasificador y mapeo a urgencia
├── README.md                                                # Este archivo
└── outputs/                                                 # Modelos y resultados generados al ejecutar el notebook
```

## Enfoque de análisis

- 🧬 **Embeddings de oración con un modelo tipo MiniLM**, en vez de bolsa de palabras clásica, para capturar significado semántico del texto libre: Reimers, N., & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*. [arXiv:1908.10084](https://arxiv.org/abs/1908.10084).
- ⚖️ **Clasificador ligero (regresión logística) sobre esos embeddings**, competitivo frente a modelos de lenguaje grandes para esta tarea específica y mucho más barato de servir: Comparación entre NLP tradicional y LLMs para clasificación de estado de salud mental, *Scientific Reports* (2025). [nature.com/articles/s41598-025-08031-0](https://www.nature.com/articles/s41598-025-08031-0).
- 📊 **Ponderación de clases por desbalance**, dado que las categorías clínicamente más urgentes tienen muchos menos ejemplos en el dataset público: técnica de ponderación de clases aplicada sobre este mismo dataset en *CPC-CMS: Cognitive Pairwise Comparison Classification Model Selection Framework*. [arXiv:2507.14022](https://arxiv.org/abs/2507.14022).

## Metas

- Construir un pipeline de clasificación de texto con embeddings preentrenados, sin necesidad de ajustar un modelo de lenguaje completo.
- Decidir con criterio cuándo un modelo ligero es más apropiado que uno grande, en función de restricciones reales de infraestructura y costo.
- Manejar correctamente un dataset desbalanceado, reportando desempeño por clase en vez de solo exactitud global.
- Trazar con claridad el límite entre lo que decide un modelo y lo que debe decidir siempre un profesional humano, en un dominio sensible como la salud mental.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=awslambda&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- 🔗 [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- 📄 [Artículo completo con el diagrama del pipeline](https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-riesgo-salud-mental-nlp-embeddings/)
- 🗂️ [Dataset público: Sentiment Analysis for Mental Health (Kaggle)](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health/data)
- 📚 Papers citados arriba (Reimers & Gurevych 2019, Scientific Reports 2025, arXiv:2507.14022)
- 📓 [`clasificacion-riesgo-salud-mental-nlp-embeddings.ipynb`](./clasificacion-riesgo-salud-mental-nlp-embeddings.ipynb)

## Cómo usar

1. Clona este repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre `clasificacion-riesgo-salud-mental-nlp-embeddings.ipynb` en Jupyter o Google Colab.
3. Descarga el dataset público [Sentiment Analysis for Mental Health desde Kaggle](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health/data) y ajusta la ruta `DATASET_PATH` en la celda de carga de datos.
4. Corre el notebook celda por celda: carga de datos → embeddings → clasificador → evaluación por clase → mapeo a nivel de urgencia.
5. Prueba la función de inferencia con un texto propio para ver a qué nivel de urgencia se clasifica.

> ⚠️ Este notebook es una demostración académica. Ninguna credencial de base de datos ni de infraestructura real se incluye aquí, y el modelo no debe usarse como herramienta de diagnóstico clínico.

---
*Made with ❤️ by FuzzyFrog.AI*
