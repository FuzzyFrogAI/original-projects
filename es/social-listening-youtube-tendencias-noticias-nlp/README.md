# 🧪 Laboratorio: Social Listening en YouTube para Tendencias de Noticias Emergentes - ATLAS FuzzyFrog.AI

**Aprende a diseñar un pipeline de NLP alrededor del costo real de una API gratuita, y a distinguir un tema que crece de forma sostenida de uno que solo tuvo un pico de volumen.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/social-listening-youtube-tendencias-noticias-nlp/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
social-listening-youtube-tendencias-noticias-nlp/
├── social-listening-youtube-tendencias-noticias-nlp.ipynb   # Notebook principal: TF-IDF, NMF, seguimiento temporal
├── outputs/
│   └── comentarios_youtube_sintetico.csv   # Dataset sintético: comentarios, categoría de referencia y fecha
└── README.md                                # Este archivo
```

## Enfoque de análisis

- 📐 **Diseñar el pipeline alrededor del costo real de cada llamada a la API.** Leer comentarios cuesta 1 unidad de cuota, buscar por palabra clave cuesta 100; esa diferencia definió el uso de canales/videos semilla en vez de búsquedas libres. Referencia: Google for Developers. *YouTube Data API Overview*. https://developers.google.com/youtube/v3/getting-started

- 🧹 **Preprocesamiento adaptado al lenguaje coloquial del comentario.** El texto de un comentario de YouTube es corto, informal y con ruido, muy distinto de un titular editorial curado, así que la limpieza se ajusta a esa naturaleza antes de vectorizar.

- 🧩 **Modelado de tópicos con NMF, sin usar ninguna etiqueta.** La factorización de matrices no negativas agrupa los comentarios en temas latentes a partir del texto, sin supervisión. Referencia: Lee, D. D., & Seung, H. S. (1999). *Learning the parts of objects by non-negative matrix factorization*. Nature, 401, 788–791. https://doi.org/10.1038/44565

- 📈 **Seguimiento temporal para distinguir tendencia de ruido.** El peso de cada tema se mide por ventana de tiempo, y solo se marca como emergente el que crece de forma sostenida, no el que solo tuvo un pico puntual. Referencia: Rieger, J., Jentsch, C., & Rahnenführer, J. (2021). *RollingLDA: An Update Algorithm of Latent Dirichlet Allocation to Construct Consistent Time Series from Textual Data*. Findings of ACL: EMNLP 2021. https://doi.org/10.18653/v1/2021.findings-emnlp.201

## Metas

- Practicar el diseño de un pipeline de datos respetando el límite real de una API gratuita (cuota, no dinero)
- Manejar credenciales de forma segura, nunca escritas directamente en el notebook
- Aplicar TF-IDF y modelado de tópicos con NMF sobre texto corto e informal
- Construir un criterio cuantitativo simple para distinguir un tema emergente de una fluctuación de corto plazo

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-scikit--learn-F7931E)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + casos de uso adicionales): https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/social-listening-youtube-tendencias-noticias-nlp/
- Papers y documentación citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `social-listening-youtube-tendencias-noticias-nlp.ipynb` y `outputs/comentarios_youtube_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `social-listening-youtube-tendencias-noticias-nlp.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/comentarios_youtube_sintetico.csv`.
4. Para conectar datos reales, define tu propia API key como variable de entorno (`YOUTUBE_API_KEY`), nunca la escribas en el notebook, y descomenta la celda de referencia en la sección 0 para reemplazar la carga del CSV.

---

*Made with ❤️ by FuzzyFrog.AI*
