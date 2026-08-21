# 🧪 Laboratorio: Asistente de Selección de Itinerarios de Viaje - ATLAS FuzzyFrog.AI

**Aprende a separar restricciones duras de preferencias suaves en un sistema de recomendación, y a diseñar una capa de personalización que pueda evolucionar de heurística a modelo entrenado sin rediseñar todo el pipeline.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/asistente-seleccion-itinerarios-viaje-recomendacion-segmentacion/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
asistente-seleccion-itinerarios-viaje-recomendacion-segmentacion/
├── asistente-seleccion-itinerarios-viaje-recomendacion-segmentacion.ipynb   # Notebook principal: espacio factible, recomendación, segmentación
├── outputs/
│   └── usuarios_preferencias_sintetico.csv   # Dataset sintético: preferencias de usuario inferidas de su historial
└── README.md                                  # Este archivo
```

## Enfoque de análisis

- 🧩 **Arquitectura de dos etapas: filtrado por restricciones, después personalización.** Separar "qué opciones son válidas" de "cuál es la mejor para este usuario" es el mismo patrón que usan los sistemas de recomendación industriales a gran escala. Referencia: Covington, P., Adams, J., & Sargin, E. (2016). *Deep Neural Networks for YouTube Recommendations*. Proceedings of the 10th ACM Conference on Recommender Systems. https://doi.org/10.1145/2959100.2959190

- 📊 **Recomendación basada en contenido (content-based filtering).** Cada opción factible se puntúa contra el vector de preferencias del usuario, sin necesitar datos de otros usuarios. Referencia: Lops, P., de Gemmis, M., & Semeraro, G. (2011). *Content-based Recommender Systems: State of the Art and Trends*. En Recommender Systems Handbook (pp. 73–105). Springer. https://doi.org/10.1007/978-0-387-85820-3_3

- 🧮 **Segmentación de usuarios con K-Means y número de perfiles elegido por evidencia.** El score de silueta decide cuántos perfiles separan mejor a los usuarios, en vez de fijar un número arbitrario. Referencia: Rousseeuw, P. J. (1987). *Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis*. Journal of Computational and Applied Mathematics, 20, 53–65. https://doi.org/10.1016/0377-0427(87)90125-7

- 🔄 **Diseñar la capa de selección para evolucionar hacia collaborative filtering.** El score heurístico actual es un punto de partida; la arquitectura ya está lista para incorporar un modelo de factorización de matrices en cuanto exista suficiente historial de decisiones reales. Referencia: Koren, Y., Bell, R., & Volinsky, C. (2009). *Matrix Factorization Techniques for Recommender Systems*. IEEE Computer, 42(8), 30–37. https://doi.org/10.1109/MC.2009.263

## Metas

- Practicar el diseño de un pipeline de recomendación en dos etapas: filtrado por reglas + personalización
- Implementar content-based filtering con un score ponderado interpretable
- Aplicar segmentación de usuarios con K-Means, eligiendo el número de grupos con evidencia estadística
- Comparar cuantitativamente dos arquitecturas de personalización sobre el mismo espacio de opciones

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-scikit--learn%20%7C%20pandas-F7931E)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + discusión de la arquitectura): https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/asistente-seleccion-itinerarios-viaje-recomendacion-segmentacion/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `asistente-seleccion-itinerarios-viaje-recomendacion-segmentacion.ipynb` y `outputs/usuarios_preferencias_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `asistente-seleccion-itinerarios-viaje-recomendacion-segmentacion.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; los catálogos de proveedores se generan dentro del notebook y las preferencias de usuario se cargan desde `outputs/usuarios_preferencias_sintetico.csv`.
4. Para probar con tu propia solicitud de viaje, modifica el diccionario `solicitud_ejemplo` en la sección de modelado y vuelve a correr desde ahí en adelante.

---

*Made with ❤️ by FuzzyFrog.AI*
