# 🧪 Laboratorio: Análisis de Sentimiento en Redes Sociales en Tiempo Real - FuzzyFrog.AI

**Objetivo:** aprender a repartir un pipeline de streaming entre un servidor persistente y funciones serverless, para minimizar el costo de infraestructura sin perder capacidad de análisis casi en vivo.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimiento-redes-sociales-tiempo-real-aws-lambda/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
analisis-sentimiento-redes-sociales-tiempo-real-aws-lambda/
├── analisis-sentimiento-redes-sociales-tiempo-real-aws-lambda.ipynb   # Notebook: NLP y análisis (traducción, sentimiento, palabra representativa)
├── outputs/
│   └── dataset_sintetico_sentimiento.csv                              # Dataset sintético de posts geolocalizados
└── README.md                                                          # Este archivo
```

## Enfoque de análisis

- 🧩 **Separación EC2 / Lambda por naturaleza de la carga:** el listener de streaming, que debe mantenerse escuchando de forma continua, vive en EC2; todo lo que se dispara por evento (traducción, sentimiento, envío al tablero) se movió a Lambda para aprovechar su capa gratuita más generosa. Referencia: Hellerstein, J. M., et al. (2019). *Serverless Computing: One Step Forward, Two Steps Back*. CIDR 2019.
- 🌐 **Traducción previa a la clasificación de sentimiento:** el texto se traduce a inglés antes de calcular la polaridad, porque el clasificador es más confiable en ese idioma que evaluando el texto original. Referencia: Pang, B., & Lee, L. (2008). *Opinion Mining and Sentiment Analysis*. Foundations and Trends in Information Retrieval, 2(1-2), 1-135.
- 📍 **Geolocalización como parte central del análisis, no como metadato extra:** el pipeline geocodifica cada registro para poder cruzar sentimiento con ubicación en el tablero, en línea con el uso de redes sociales como sensor social en tiempo real. Referencia: Sakaki, T., Okazaki, M., & Matsuo, Y. (2010). *Earthquake shakes Twitter users: real-time event detection by social sensors*. WWW 2010, 851-860.
- 📦 **Formato de intercambio con delimitadores de texto en lugar de JSON estructurado:** decisión pragmática para simplificar la etapa de streaming, documentada honestamente como una limitación real (ver sección "Proceso de iteración" del artículo).

## Metas

- Diseñar un pipeline de datos en tiempo real repartido entre cómputo persistente y serverless.
- Aplicar análisis de sentimiento sobre texto en español con un paso de traducción intermedio.
- Construir un dataset sintético que preserve la estructura y el comportamiento de datos reales, sin exponerlos.
- Reconocer honestamente los trade-offs de un formato de datos simplificado frente a uno estructurado.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)
![AWS](https://img.shields.io/badge/Cloud-AWS%20Lambda%20%7C%20S3%20%7C%20Firehose-yellow)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimiento-redes-sociales-tiempo-real-aws-lambda/)
- Papers citados en "Enfoque de análisis" (ver arriba)
- Notebook: `analisis-sentimiento-redes-sociales-tiempo-real-aws-lambda.ipynb`

## Cómo usar

1. Clona este repositorio.
2. Abre `analisis-sentimiento-redes-sociales-tiempo-real-aws-lambda.ipynb` en Jupyter o Google Colab.
3. Corre todas las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/`.
4. Prueba la función `analyze_post()` con tu propio texto para ver la traducción, polaridad y palabra representativa que generaría.

---

*Made with ❤️ by FuzzyFrog.AI*
