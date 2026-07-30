# 🧪 Laboratorio: Predicción de Precipitación con Datos Abiertos - ATLAS FuzzyFrog.AI

**Objetivo:** aprender a comprobar con evidencia si un producto satelital abierto mejora un modelo de precipitación local, en vez de asumir su valor solo porque está disponible gratis.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/ambiente/prediccion-precipitacion-datos-abiertos-cuencas-hidrograficas/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
prediccion-precipitacion-datos-abiertos-cuencas-hidrograficas/
├── prediccion-precipitacion-datos-abiertos-cuencas-hidrograficas.ipynb   # Notebook ejecutable, extremo a extremo
├── outputs/
│   └── dataset_sintetico_precipitacion.csv                                # Dataset sintético, estación propia y proxy de dato abierto
└── README.md                                                              # Este archivo
```

## Enfoque de análisis

- 🛰️ **GPCC y CHIRPS como datos abiertos complementarios.** Son productos que combinan estaciones reales de todo el mundo con estimación satelital, con metodología publicada abiertamente, lo que los hace confiables para enriquecer un dataset propio. Referencia: Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., Husak, G., Rowland, J., Harrison, L., Hoell, A., & Michaelsen, J. 2015. The climate hazards infrared precipitation with stations, a new environmental record for monitoring extremes. Scientific Data, 2, 150066. https://doi.org/10.1038/sdata.2015.66
- 🌳 **Random Forest para una serie mensual corta.** Con pocos años de historial, un modelo de árboles tolera mejor el ruido y la escasez de datos que una arquitectura con muchos parámetros que ajustar. Referencia: Breiman, L. 2001. Random Forests. Machine Learning, 45(1), 5 a 32. https://doi.org/10.1023/A:1010933404324
- 🗺️ **Shapefile y KML como contexto cartográfico, no como variable del modelo.** Ambos formatos son estándares abiertos ampliamente documentados para representar geometría geográfica, y aquí se usan para confirmar la representatividad espacial de la estación, no para alimentar la predicción. Referencia: Open Geospatial Consortium. 2008. OGC KML, Version 2.2.0. Referencia técnica del formato Shapefile: ESRI. 1998. ESRI Shapefile Technical Description.
- 📊 **Comparación con y sin dato abierto antes de decidir el diseño final.** Agregar una fuente de datos externa incrementa la complejidad de cualquier sistema, y esa complejidad solo se justifica cuando mejora un resultado medible. Referencia: Sculley, D., Holt, G., Golovin, D., et al. 2015. Hidden technical debt in machine learning systems. Advances in Neural Information Processing Systems, 28.

## Metas

- Practicar el hábito de medir, en vez de asumir, si una fuente de datos externa mejora un modelo propio.
- Aprender a combinar una serie de estación con un producto satelital de menor resolución sin perder la señal local.
- Entender la diferencia entre una variable que alimenta un modelo y un dato cartográfico que solo da contexto para interpretar el resultado.
- Practicar el manejo honesto de resultados modestos, sin inflar una mejora pequeña para que suene mejor de lo que es.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![geopandas](https://img.shields.io/badge/geopandas-GIS-00b76c)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-006a87)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del caso](https://fuzzyfrog.ai/es/ai-lab/proyectos/ambiente/prediccion-precipitacion-datos-abiertos-cuencas-hidrograficas/)
- Referencias citadas arriba en Enfoque de análisis
- [`prediccion-precipitacion-datos-abiertos-cuencas-hidrograficas.ipynb`](./prediccion-precipitacion-datos-abiertos-cuencas-hidrograficas.ipynb)

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `prediccion-precipitacion-datos-abiertos-cuencas-hidrograficas.ipynb` en Jupyter, Google Colab o VS Code.
3. Ejecuta todas las celdas en orden. El dataset sintético se genera dentro del propio notebook y no requiere descargas externas.
4. Para probarlo con tu propia cuenca, reemplaza la serie sintética de estación por tu registro real, y sustituye el proxy satelital por una extracción real de GPCC o CHIRPS en las coordenadas de tu punto de interés.
5. Reemplaza el polígono sintético de la cuenca por tu shapefile o tu archivo KML real usando geopandas, manteniendo el mismo flujo de verificación de contención de la estación dentro del polígono.

---
*Made with ❤️ by FuzzyFrog.AI*
