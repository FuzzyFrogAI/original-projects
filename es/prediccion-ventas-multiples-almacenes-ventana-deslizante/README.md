# 🧪 Laboratorio: Predicción de Ventas en Múltiples Almacenes - ATLAS FuzzyFrog.AI

**Aprende a convertir decenas de series de ventas en un problema de regresión con ventana deslizante, y por qué medir el sesgo del modelo (BIAS) puede importar más que medir su error para decisiones de inventario.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-multiples-almacenes-ventana-deslizante/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
prediccion-ventas-multiples-almacenes-ventana-deslizante/
├── prediccion-ventas-multiples-almacenes-ventana-deslizante.ipynb   # Notebook principal: ventana deslizante, comparación de modelos
├── outputs/
│   └── ventas_almacenes_sintetico.csv   # Dataset sintético: ventas mensuales por almacén y producto
└── README.md                             # Este archivo
```

## Enfoque de análisis

- 🪟 **Ventana deslizante para convertir cada serie en regresión tabular.** 12 meses de historia como entrada, el mes siguiente como objetivo, aplicable con el mismo código a cualquier combinación de almacén y producto. Referencia: *Improving Time Series Forecasting by Applying the Sliding Window Approach*. Springer Nature Link. https://link.springer.com/chapter/10.1007/978-3-031-98304-7_34

- 📊 **BIAS como métrica adicional a RMSE.** Dos modelos con el mismo error promedio pueden tener implicaciones de negocio muy distintas si uno sub-pronostica y el otro sobre-pronostica de forma sistemática. Referencia: Hyndman, R. J., & Koehler, A. B. (2006). *Another look at measures of forecast accuracy*. International Journal of Forecasting, 22(4), 679–688. https://doi.org/10.1016/j.ijforecast.2006.03.001

- 🌲 **Comparación de 4 familias de modelos con la misma metodología.** Regresión Lineal, Árbol de Decisión, Random Forest y Red Neuronal, evaluados sobre exactamente las mismas ventanas de entrenamiento y prueba. Referencia: *Optimization of Forecasting Performance in the Retail Sector Using Artificial Intelligence*. Engineering Proceedings. https://doi.org/10.3390/engproc2025112037

- 🔍 **Ajuste de hiperparámetros de forma sistemática, no manual.** Búsqueda en grilla con validación cruzada para los modelos más sensibles a sus hiperparámetros, en vez de probar combinaciones a mano. Referencia: Bergstra, J., & Bengio, Y. (2012). *Random Search for Hyper-Parameter Optimization*. Journal of Machine Learning Research, 13, 281–305.

## Metas

- Practicar la construcción de ventanas deslizantes para convertir series de tiempo en problemas de regresión
- Comparar varias familias de modelos con una metodología de evaluación consistente
- Entender por qué RMSE por sí solo no basta para decisiones de inventario, y cómo el BIAS complementa esa evaluación
- Reconocer cuándo una decisión de modelo depende del contexto de negocio y no solo de la métrica de error más común

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-scikit--learn-F7931E)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + discusión sobre error vs. sesgo): https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-multiples-almacenes-ventana-deslizante/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `prediccion-ventas-multiples-almacenes-ventana-deslizante.ipynb` y `outputs/ventas_almacenes_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `prediccion-ventas-multiples-almacenes-ventana-deslizante.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/ventas_almacenes_sintetico.csv`.
4. Para probar el pipeline con tu propio historial de ventas, respeta las columnas (`almacen`, `producto`, `periodo`, `ventas`) y vuelve a correr desde la sección de modelado; la ventana deslizante y las métricas se recalculan automáticamente para cada combinación.

---

*Made with ❤️ by FuzzyFrog.AI*
