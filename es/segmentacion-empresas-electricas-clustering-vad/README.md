# 🧪 Laboratorio: Segmentación de Empresas Eléctricas con Clustering Aplicado al VAD - ATLAS FuzzyFrog.AI

**Aprenderás a usar clustering para agrupar empresas de una industria regulada según su estructura de costos, entendiendo primero el criterio detrás del problema antes de tocar el modelo.**

🔗 [Plataforma](https://fuzzyfrog.ai/es/) | 📄 [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/segmentacion-empresas-electricas-clustering-vad/) | 📁 [Todos los proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
segmentacion-empresas-electricas-clustering-vad/
├── segmentacion-empresas-electricas-clustering-vad.ipynb   # Notebook ejecutable: clustering y exploración de perfil de carga
├── 91_DataIn_sintetico.csv                                 # Indicadores sintéticos por empresa (VADT, CxK)
├── Perfil_alimentador_sintetico.csv                        # Perfil de carga sintético de un alimentador
├── README.md                                                # Este archivo
└── outputs/                                                  # Resultados generados al ejecutar el notebook
```

## Enfoque de análisis

- ⚡ **Clustering aplicado a benchmarking regulatorio de empresas de distribución eléctrica**, agrupando firmas con estructura de costos similar antes de compararlas: Dai, X., & Kuosmanen, T. (2014). *Best-practice benchmarking using clustering methods: Application to energy regulation*. Omega, 42, 179-188. [doi:10.1016/j.omega.2013.05.007](https://doi.org/10.1016/j.omega.2013.05.007).
- 🔍 **K-Means como algoritmo de agrupación**, sobre variables normalizadas para evitar que la escala domine la distancia: MacQueen, J. (1967). *Some methods for classification and analysis of multivariate observations*. Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, 1, 281-297.
- 📊 **Clustering como herramienta de segmentación en distribuidoras eléctricas de otros mercados regulados**, con hallazgos similares sobre la heterogeneidad de las empresas: *A clustering scheme for performance benchmarking in the regulation of electric distribution utilities*, ScienceDirect (2025). [sciencedirect.com/science/article/abs/pii/S0957178724001759](https://www.sciencedirect.com/science/article/abs/pii/S0957178724001759).

## Metas

- Entender el criterio regulatorio detrás de un problema antes de diseñar el modelo de clustering.
- Normalizar variables correctamente para que ninguna domine la distancia del algoritmo por su escala.
- Elegir un número de clústeres con criterio explícito, sin asumir que debe coincidir con una clasificación oficial más compleja.
- Reconocer cuándo los datos de un proyecto vienen de una empresa real, y aplicar anonimización o datos sintéticos en consecuencia.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- 🔗 [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- 📄 [Artículo completo con el diagrama del pipeline](https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/segmentacion-empresas-electricas-clustering-vad/)
- 📚 Papers citados arriba (Dai & Kuosmanen 2014, MacQueen 1967, ScienceDirect 2025)
- 📓 [`segmentacion-empresas-electricas-clustering-vad.ipynb`](./segmentacion-empresas-electricas-clustering-vad.ipynb)

## Cómo usar

1. Clona este repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Entra a la carpeta del proyecto y abre `segmentacion-empresas-electricas-clustering-vad.ipynb` en Jupyter o Google Colab.
3. Los archivos CSV incluidos son sintéticos. Si tienes tus propios indicadores de empresa, respeta siempre la autorización y anonimización correspondiente antes de usarlos.
4. Corre el notebook celda por celda: carga de datos → EDA → clustering → evaluación visual → exploración del perfil de carga.
5. Ajusta el número de clústeres y compara el resultado contra el criterio de agrupación que tenga sentido para tu propio contexto regulatorio o de negocio.

---
*Made with ❤️ by FuzzyFrog.AI*
