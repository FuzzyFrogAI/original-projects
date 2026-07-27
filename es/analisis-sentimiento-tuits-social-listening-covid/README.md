# 🧪 Laboratorio: Análisis de Sentimiento en Tuits para Social Listening - ATLAS FuzzyFrog.AI

**Aprenderás a construir un pipeline de social listening y a elegir el modelo correcto mirando más allá de la exactitud global, sobre todo cuando las clases están desbalanceadas.**

🔗 [Plataforma](https://fuzzyfrog.ai/es/) | 📄 [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimiento-tuits-social-listening-covid/) | 📁 [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
analisis-sentimiento-tuits-social-listening-covid/
├── analisis-sentimiento-tuits-social-listening-covid.ipynb   # Notebook ejecutable: limpieza, etiquetado, modelado y comparación
├── README.md                                                 # Este archivo
└── outputs/                                                  # Resultados y modelos generados al ejecutar el notebook
```

## Enfoque de análisis

- 🌎 **Modernización del etiquetado de sentimiento con un modelo nativo en español**, evitando la traducción palabra por palabra al inglés del enfoque original: Pérez, J.M., Rajngewerc, M., Giudici, J.C., et al. (2021). *pysentimiento: A Python Toolkit for Sentiment Analysis and SocialNLP tasks*. [arXiv:2106.09462](https://arxiv.org/abs/2106.09462).
- ⚖️ **Elegir el clasificador por desempeño por clase, no solo por exactitud global**, en un problema con clases desbalanceadas: Japkowicz, N., & Stephen, S. (2002). *The class imbalance problem: A systematic study*. Intelligent Data Analysis, 6(5), 429-449.
- 🔒 **Manejo ético de datos públicos de redes sociales**, incluyendo la protección de identidad de terceros y la transparencia sobre los límites del método: Franzke, A.S., Bechmann, A., Zimmer, M., Ess, C., & Association of Internet Researchers (2020). *Internet Research: Ethical Guidelines 3.0*.

## Metas

- Construir un pipeline completo de social listening, desde la recolección de texto hasta la comparación de modelos.
- Reconocer cuándo una etiqueta de entrenamiento es una heurística y no una verdad de campo, y comunicarlo con honestidad.
- Comparar clasificadores clásicos mirando precisión y recall por clase, no solo la exactitud global.
- Aplicar un manejo ético consistente a datos públicos de redes sociales, protegiendo la identidad de terceros.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- 🔗 [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- 📄 [Artículo completo con el diagrama del pipeline](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocio/analisis-sentimiento-tuits-social-listening-covid/)
- 📚 Papers citados arriba (Pérez et al. 2021, Japkowicz & Stephen 2002, Franzke et al. 2020)
- 📓 [`analisis-sentimiento-tuits-social-listening-covid.ipynb`](./analisis-sentimiento-tuits-social-listening-covid.ipynb)

## Cómo usar

1. Clona este repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre `analisis-sentimiento-tuits-social-listening-covid.ipynb` en Jupyter o Google Colab.
3. El notebook usa una muestra sintética de ejemplo en vez de tuits reales. Si tienes acceso vigente a una API de datos sociales, sustitúyela por tu propia fuente, respetando siempre los términos de uso y la privacidad de terceros.
4. Corre el notebook celda por celda: limpieza → etiquetado → representación de texto → comparación de clasificadores → elección del modelo.
5. Revisa siempre el desempeño por clase antes de confiar en cualquier modelo de clasificación de sentimiento.

> ⚠️ Ninguna credencial de API se incluye en este notebook. Nunca coloques claves de acceso en texto plano en un notebook que vayas a compartir.

---
*Made with ❤️ by FuzzyFrog.AI*
