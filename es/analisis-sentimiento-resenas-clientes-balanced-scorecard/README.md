# 🧪 Laboratorio: Reseñas de Clientes a Tablero de Decisión Estratégica - FuzzyFrog.AI

**Objetivo:** aprender a convertir reseñas de clientes en varios idiomas en indicadores de negocio accionables, combinando NLP no supervisado con validación experta.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimiento-resenas-clientes-balanced-scorecard/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
analisis-sentimiento-resenas-clientes-balanced-scorecard/
├── analisis-sentimiento-resenas-clientes-balanced-scorecard.ipynb   # Notebook: limpieza, traducción, sentimiento y clustering
├── outputs/
│   └── dataset_sintetico_resenas_multiidioma.csv                    # Dataset sintético de reseñas en varios idiomas
└── README.md                                                        # Este archivo
```

## Enfoque de análisis

- 🌐 **Traducción previa al análisis de sentimiento:** cada reseña se detecta y se traduce a inglés antes de calcular su polaridad, porque el analizador léxico usado rinde mejor en ese idioma que evaluando texto multiidioma sin normalizar. Referencia de la técnica: Hutto, C. J., & Gilbert, E. (2014). VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text. Eighth International AAAI Conference on Weblogs and Social Media.
- 🧩 **Clustering no supervisado sobre una matriz de frecuencia de términos:** en lugar de resumir el corpus con un conteo simple de palabras, se agrupan las reseñas por similitud de vocabulario para descubrir temas que conviven en los datos sin etiquetas previas.
- 🤝 **Validación del significado de negocio junto con el cliente:** el significado de cada cluster y de cada tendencia de sentimiento se valida con el equipo del negocio antes de mapearlo a un indicador, en vez de asumir que el resultado técnico ya es la decisión final.
- 📋 **Documentación honesta de los límites de la detección automática de idioma:** un caso de texto sin estructura reconocible se identificó y se descartó manualmente, en lugar de forzar un resultado.

Si quieres ver un enfoque publicado que combina sentimiento de reseñas con modelos de decisión aplicados a un caso de restaurantes, esta referencia es un buen punto de comparación del tipo de problema: Zuheros, C., Martínez-Cámara, E., Herrera-Viedma, E., & Herrera, F. (2021). Sentiment analysis based multi-person multi-criteria decision making methodology using natural language processing and deep learning for smarter decision aid. Information Fusion, 68, 22-36.

## Metas

- Limpiar y normalizar datos de texto exportados con estructura irregular.
- Aplicar detección de idioma y traducción como paso previo a un análisis de sentimiento multiidioma.
- Descubrir temas en texto no etiquetado usando una matriz de frecuencia de términos y clustering no supervisado.
- Reconocer cuándo un resultado técnico necesita validación de negocio antes de convertirse en un indicador.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)
![NLP](https://img.shields.io/badge/NLP-NLTK%20%7C%20TextBlob%20%7C%20scikit--learn-yellow)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimiento-resenas-clientes-balanced-scorecard/)
- Referencias citadas en "Enfoque de análisis" (ver arriba)
- Notebook: `analisis-sentimiento-resenas-clientes-balanced-scorecard.ipynb`

## Cómo usar

1. Clona este repositorio.
2. Abre `analisis-sentimiento-resenas-clientes-balanced-scorecard.ipynb` en Jupyter o Google Colab.
3. Corre todas las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/`.
4. Revisa la celda de interpretación de clusters y compárala con tu propio criterio de negocio antes de mapear cualquier resultado a un indicador.

---

*Made with ❤️ by FuzzyFrog.AI*
