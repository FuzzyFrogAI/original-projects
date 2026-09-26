# 🧪 Laboratorio: Predicción de ventas, detección de anomalías y segmentación de clientes - ATLAS FuzzyFrog.AI

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![LightGBM](https://img.shields.io/badge/LightGBM-scikit--learn-9ACD32.svg)](https://lightgbm.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ATLAS FuzzyFrog.AI](https://img.shields.io/badge/ATLAS-FuzzyFrog.AI-00b76c.svg)](https://fuzzyfrog.ai/es/)

**Aprende a medir cada técnica con la pregunta que de verdad responde: un pronóstico contra el pronóstico ingenuo, un detector de anomalías contra anomalías conocidas, y una segmentación contra lo que los clientes hacen después.**

## Qué vas a aprender

Un mismo historial de ventas responde tres preguntas de negocio distintas: cuánto se va a vender de cada producto el mes que viene, qué días algo no encaja y qué tipos de cliente tiene el negocio. En el camino tocas backtesting con origen móvil, modelos globales para muchas series cortas, detección robusta sobre residuos y RFM con validación fuera de periodo.

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-segmentacion-anomalias/) | [Todos los proyectos](https://fuzzyfrog.ai/es/ai-lab/proyectos/)

## Estructura del laboratorio

```
es/prediccion-ventas-segmentacion-anomalias/
├── README.md                                    ← este archivo
├── prediccion_ventas_segmentacion_anomalias.ipynb  ← notebook completo: pronóstico, anomalías y segmentación
├── diagrama-solucion.svg                        ← diagrama del pipeline (fuente editable, mismo diseño que el artículo)
├── requirements.txt                             ← dependencias con versión fija
└── data/
    ├── ventas_sinteticas.csv                    ← transacciones sintéticas, 5 años, 4 sucursales
    ├── anomalias_inyectadas.csv                 ← anomalías conocidas inyectadas, solo para evaluar (ningún modelo las ve)
    └── segmento_real_clientes.csv               ← tipo real de cliente del generador, solo para evaluar la segmentación
```

## Enfoque de análisis

- 📈 **Pronóstico mensual con modelo global** sobre 20 productos, comparado contra tres referencias sin aprendizaje y evaluado con backtest de origen móvil, WAPE y MASE. Makridakis, S., Spiliotis, E. & Assimakopoulos, V. (2022). *M5 accuracy competition: Results, findings, and conclusions*. International Journal of Forecasting.
- 📏 **MASE como métrica de referencia estacional**, para saber si un modelo mejora de verdad al pronóstico "mismo mes del año anterior". Hyndman, R. J. & Koehler, A. B. (2006). *Another look at measures of forecast accuracy*. International Journal of Forecasting.
- 🚨 **Detección de anomalías con z robusto sobre el residuo y rachas de días sin venta**, usando la desviación absoluta mediana en vez de la desviación estándar. Iglewicz, B. & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
- 🧮 **Segmentación de clientes con RFM**, comparando K-means, mezcla gaussiana y reglas por quintiles, validadas contra la recompra real de un periodo posterior. Fader, P. S., Hardie, B. G. S. & Lee, K. L. (2005). *RFM and CLV: Using Iso-value Curves for Customer Base Analysis*. Journal of Marketing Research.

## Explora las decisiones alternativas

Cada decisión de abajo se corrió con todas sus opciones dentro del notebook. En el artículo puedes proponer tu propia alternativa antes de ver qué hubiera pasado:

- **¿Pronosticar por día o por mes?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-segmentacion-anomalias/#explorador-nivel_agregacion)
- **¿Un modelo por producto o un modelo global?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-segmentacion-anomalias/#explorador-modelo_global)
- **¿Con qué métrica elegir el modelo: MAPE, WAPE o MASE?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-segmentacion-anomalias/#explorador-metrica_pronostico)
- **¿Qué método de detección de anomalías usar?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-segmentacion-anomalias/#explorador-deteccion_anomalias)
- **¿K-means, mezcla gaussiana o reglas RFM por quintiles?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-segmentacion-anomalias/#explorador-segmentacion_metodo)

## Metas

Al recorrer este repo vas a practicar:

- Diseñar un backtest de origen móvil que nunca mezcla meses futuros con el entrenamiento.
- Decidir entre un modelo por serie o un modelo global cuando tienes muchas series cortas, y probar la diferencia con bootstrap en vez de asumirla.
- Elegir la métrica de pronóstico según lo que de verdad le importa al negocio, no la más fácil de calcular.
- Construir un detector de anomalías que distingue un evento real (una pandemia) de un error, y que encuentra tanto picos como rachas de silencio.
- Validar una segmentación contra comportamiento futuro real, no solo contra qué tan separados quedan los grupos.

## Recursos

- **Plataforma**: [fuzzyfrog.ai](https://fuzzyfrog.ai/es/)
- **Artículo completo**: [¿Cómo detectar anomalías en ventas mientras se predice y segmenta al mismo tiempo?](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-ventas-segmentacion-anomalias/)
- **Papers citados**: ver [Enfoque de análisis](#enfoque-de-análisis) arriba.
- **Notebook**: [`prediccion_ventas_segmentacion_anomalias.ipynb`](prediccion_ventas_segmentacion_anomalias.ipynb)

## Cómo usar

```bash
git clone https://github.com/FuzzyFrogAI/original-projects.git
cd original-projects/es/prediccion-ventas-segmentacion-anomalias
pip install -r requirements.txt
jupyter notebook prediccion_ventas_segmentacion_anomalias.ipynb
```

1. Clona el monorepo e instala las dependencias fijas de `requirements.txt`. No necesita GPU.
2. Abre `prediccion_ventas_segmentacion_anomalias.ipynb` (en Jupyter local o subiéndolo a Google Colab).
3. Córrelo de arriba a abajo. La celda 0 fija semilla y todas las decisiones numéricas del experimento. Si el CSV de `data/` ya existe se carga de ahí; si no, se genera con la semilla fija.
4. Al final, el notebook exporta `explorador_resultados.json`: son los números de cada decisión alternativa, la misma fuente que usa el Explorador de decisiones del artículo.

---

Made with 💚 by FuzzyFrog.AI
