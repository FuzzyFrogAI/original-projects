# 🧪 Laboratorio: Clasificación Automática de PQRS con NLP - FuzzyFrog.AI

**Aprende a resolver con un experimento, no con una suposición, si el orden de los pasos de preprocesamiento de texto afecta el resultado final.**

🔗 Enlaces rápidos: [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/gobierno/clasificacion-automatica-pqrs-nlp-bag-of-words/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```plaintext
clasificacion-automatica-pqrs-nlp-bag-of-words/
├── README.md                                              ← este archivo
├── clasificacion-automatica-pqrs-nlp-bag-of-words.ipynb    ← notebook completo, ejecutable en Colab
└── dataset/
    ├── pqrs_sintetico.csv                                  ← dataset sintético de PQRS
    └── comparacion_modelos_pqrs.csv                        ← accuracy por modelo (validación cruzada)
```

## Enfoque de análisis

- 🔤 **Orden de preprocesamiento validado con un experimento, no una suposición.** Se probó lematizar antes y después de remover acentos sobre la misma muestra, y se documentó la diferencia real encontrada. Referencia: [Manning, C. et al. (2008). *Introduction to Information Retrieval*, capítulo de normalización de texto.](https://nlp.stanford.edu/IR-book/)
- 📊 **Comparación honesta contra el nivel de azar.** Con un dataset pequeño y varias categorías, el accuracy de cualquier modelo se interpreta siempre contra la probabilidad de acertar al azar, no de forma aislada. Referencia: [Kim, N. & Hong, S. (2021). *Automatic classification of citizen requests for transportation using deep learning*.](https://doi.org/10.1016/J.IPM.2020.102410)
- ⚖️ **Bag-of-words simple antes que embeddings complejos.** Se prioriza un vectorizador simple sobre uno más sofisticado cuando el dataset no tiene el tamaño suficiente para aprovechar la complejidad adicional.

## Metas

- Practicar el preprocesamiento correcto de texto en español (lematización, manejo de acentos, stopwords) con spaCy.
- Aprender a comparar modelos de clasificación de texto con validación cruzada sobre datasets pequeños.
- Entender por qué un accuracy debe interpretarse siempre contra el nivel de azar, no de forma aislada.
- Practicar la resolución de dudas técnicas con experimentos directos, en vez de suposiciones.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-NLP%20en%20espa%C3%B1ol-09A3D5?logo=spacy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-5%20modelos-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter%2FColab-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/gobierno/clasificacion-automatica-pqrs-nlp-bag-of-words/)
- Referencias citadas en Enfoque de análisis (ver arriba)
- Notebook: `clasificacion-automatica-pqrs-nlp-bag-of-words.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Abre `clasificacion-automatica-pqrs-nlp-bag-of-words.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden — instalan spaCy y el modelo de español automáticamente.
4. Para usar tus propios datos, reemplaza el CSV de entrada conservando las columnas `Texto` y `Tipo de solicitud`.

---

*Made with ❤️ by FuzzyFrog.AI*
