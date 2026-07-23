# 🧪 Laboratorio: Mapas de Prospectividad Mineral con Datos Geoespaciales - ATLAS FuzzyFrog.AI

**Aprende a construir un mapa de prospectividad mineral con litología, campo magnético y geoquímica, usando interpolación espacial, clustering y regresión, partiendo de datos mínimos y abiertos.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/mapas-prospectividad-mineral-machine-learning/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
mapas-prospectividad-mineral-machine-learning/
├── mapas-prospectividad-mineral-machine-learning.ipynb   # Notebook: carga, grid, interpolación, 3 modelos y hallazgos
├── data/
│   ├── litologia.shp         # Shapefile de ejemplo, sustituir por datos propios
│   ├── campo_magnetico.shp   # Shapefile de ejemplo, sustituir por datos propios
│   └── geoquimica.shp        # Shapefile de ejemplo, sustituir por datos propios
└── README.md
```

## Enfoque de análisis

- 🗺️ **Rejilla uniforme con tamaño de celda justificado, no por default.** El tamaño se fija según la resolución real de los datos, no un valor arbitrario. Referencia: Hengl, T. (2006). Finding the right pixel size. *Computers & Geosciences, 32*(9), 1283-1298.
- 📐 **Dos métodos de interpolación, uno por tipo de señal.** IDW para campo magnético, RBF con base gaussiana para geoquímica. Referencia: Shepard, D. (1968). A two-dimensional interpolation function for irregularly-spaced data. *Proceedings of the 1968 23rd ACM National Conference*.
- 🔍 **DBSCAN como contraste a KMeans para detectar anomalías sin forma predefinida.** Referencia: Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining (KDD-96)*.
- 🌲 **Comparación de múltiples regresores en vez de asumir linealidad.** Referencia: Sun, T., Chen, F., Zhong, L. X., Liu, W. M., & Wang, Y. (2019). GIS-based mineral prospectivity mapping using machine learning methods: A case study from Tongling ore district, eastern China. *Ore Geology Reviews, 109*, 26-49.

## Metas

- Practicar la construcción de una rejilla uniforme sobre un área de trabajo geoespacial y justificar el tamaño de celda con criterio, no con un default.
- Aprender cuándo usar IDW y cuándo usar RBF según el comportamiento espacial real de la variable.
- Ver un ejemplo real de cuándo un enfoque no supervisado (KMeans + DBSCAN) es preferible a forzar una clasificación supervisada sin suficientes datos etiquetados.
- Entender por qué combinar varias señales de modelado en un mapa final, en vez de quedarte con la mejor de las tres por separado, produce un resultado más honesto.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![GeoPandas](https://img.shields.io/badge/GeoPandas-Análisis%20espacial-139C5A?logo=python&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-KMeans%20%2B%20DBSCAN%20%2B%20Regresión-F7931E?logo=scikitlearn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-IDW%20%2B%20RBF-8CAAE6?logo=scipy&logoColor=white)
![Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/mapas-prospectividad-mineral-machine-learning/)
- Papers citados en "Enfoque de análisis" arriba
- `mapas-prospectividad-mineral-machine-learning.ipynb` (notebook principal)

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Sustituye los shapefiles de `data/` por tus propios datos de litología, campo magnético y geoquímica, manteniendo el mismo esquema de columnas.
3. Abre `mapas-prospectividad-mineral-machine-learning.ipynb` en Jupyter o Google Colab.
4. Corre las celdas en orden: carga de datos → grid uniforme → interpolación (IDW y RBF) → los tres enfoques de modelado (KMeans, DBSCAN, regresión) → mapa de prospectividad combinado.
5. Para probar con tus propios elementos geoquímicos de interés, ajusta el nombre de columna en la celda de interpolación RBF.

---
*Made with ❤️ by FuzzyFrog.AI*
