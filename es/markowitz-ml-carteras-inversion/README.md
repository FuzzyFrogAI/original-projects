# 🧪 Laboratorio: Optimización de Carteras con LSTM, CAPM y Markowitz - ATLAS FuzzyFrog.AI

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras%20LSTM-FF6F00?logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Preprocesamiento-F7931E?logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Optimizaci%C3%B3n%20SLSQP-8CAAE6)
![yfinance](https://img.shields.io/badge/yfinance-Datos%20abiertos-800080)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-006a87)

**Objetivo:** aprender a construir un pipeline completo de asignación de portafolio, desde la predicción de rendimientos esperados con un modelo de series de tiempo hasta la optimización de pesos, y a justificar cada decisión con criterio propio en vez de copiarla.

## Qué vas a aprender

Vas a ver, con datos reales, cómo se conecta una predicción de series de tiempo con una decisión de asignación de portafolio, y por qué cada bisagra del pipeline se resolvió de una forma y no de otra. De paso, entras en contacto con tres piezas que reaparecen en muchos problemas distintos: cuándo un LSTM vale la pena frente a algo más simple, qué indicadores técnicos aportan señal sobre una serie de precios y qué mide en realidad el CAPM. La idea no es que memorices esta receta, sino que salgas pudiendo armar la tuya.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/) | [Article in English](https://fuzzyfrog.ai/en/ai-lab/proyectos/business/markowitz-ml-portfolio-optimization/) | [Notebook en Colab](https://colab.research.google.com/drive/1mFF8xIFR8aaeIAxjeAHtza6P6Tj6Y4Kf?usp=sharing) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
markowitz-ml-carteras-inversion/
├── markowitz-ml-carteras-inversion.ipynb   # Notebook ejecutable, extremo a extremo
├── diagrama-solucion.drawio                 # Diagrama editable del pipeline (mismo que el del artículo)
├── requirements.txt                         # Dependencias para correrlo fuera de Colab
└── README.md                                # Este archivo
```

No hay carpeta `/data`: los precios se descargan en vivo desde yfinance dentro del propio notebook, así que no se distribuye ningún dataset ni sintético ni real junto con este repositorio.

## Explora las decisiones alternativas

Cada una de las siguientes preguntas tiene su propio Explorador de decisiones interactivo en el artículo, con el resultado de la opción elegida y de la alternativa. Estas mismas preguntas están replicadas en el notebook, en el punto exacto del pipeline donde se toma cada decisión, para que las pienses antes de ver la celda siguiente.

1. **¿Solo precio de cierre o con indicadores técnicos?** → [Explorar esta decisión](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-lstm_indicadores)
2. **¿Cuántas capas LSTM y cuántas unidades?** → [Explorar esta decisión](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-lstm_arquitectura)
3. **¿Incluir todos los activos en Markowitz o filtrar antes con CAPM?** → [Explorar esta decisión](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-capm_filtro)
4. **¿Minimizar volatilidad o maximizar el ratio de Sharpe?** → [Explorar esta decisión](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-markowitz_objetivo)

## Enfoque de análisis

- 📈 **Indicadores técnicos como features del LSTM, no solo el precio de cierre.** SMA de 20 días, Bandas de Bollinger (20 días, 2σ), RSI de 14 días y autocorrelación de rezago 1, calculados por acción antes de entrenar, para que el modelo vea momentum y volatilidad además del nivel de precio. Referencia: Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.
- 🔁 **Un LSTM de tres capas por acción, entrenado de forma independiente.** Tres capas apiladas de 50 unidades con Dropout progresivo se prefirieron sobre una arquitectura de una sola capa por su mayor capacidad de representación, a costa de más tiempo de entrenamiento. Referencia: Hochreiter, S., & Schmidhuber, J. (1997). *Long Short-Term Memory*. Neural Computation, 9(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735
- 📊 **Filtro CAPM antes de optimizar, no después.** El beta de cada activo se estimó por regresión lineal contra el S&P 500 como proxy de mercado, y solo los activos con premio por riesgo justificado entraron al optimizador, para reducir la inestabilidad numérica de Markowitz en universos grandes. Referencia: Sharpe, W. F. (1964). *Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk*. The Journal of Finance, 19(3), 425–442. https://doi.org/10.1111/j.1540-6261.1964.tb02865.x
- ⚖️ **Optimización de mínima volatilidad sobre la Frontera Eficiente, no máximo Sharpe.** Con `scipy.optimize.minimize` (SLSQP) sobre la matriz de covarianza, se eligió el punto más conservador de la frontera por ser numéricamente más estable frente a la incertidumbre de un rendimiento esperado que viene de una predicción. Referencia: Markowitz, H. (1952). *Portfolio Selection*. The Journal of Finance, 7(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x

## Metas

- Practicar el diseño de un pipeline donde la salida de un modelo de predicción alimenta directamente una decisión de optimización, y entender qué error se propaga y dónde.
- Aprender a decidir cuándo un indicador técnico agrega señal real a una serie de precios y cuándo solo agrega ruido y NaN.
- Entender qué mide el CAPM, para qué sirve como filtro previo a Markowitz y cuáles son sus supuestos.
- Comparar minimizar volatilidad contra maximizar el ratio de Sharpe como objetivos de optimización, y saber justificar cuál usar según la calidad del rendimiento esperado con el que se cuenta.

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del caso, en español](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/)
- [Full article, in English](https://fuzzyfrog.ai/en/ai-lab/proyectos/business/markowitz-ml-portfolio-optimization/)
- Papers citados arriba, en la sección Enfoque de análisis
- [Notebook en Google Colab](https://colab.research.google.com/drive/1mFF8xIFR8aaeIAxjeAHtza6P6Tj6Y4Kf?usp=sharing)
- [`diagrama-solucion.drawio`](./diagrama-solucion.drawio), editable con [draw.io](https://app.diagrams.net/)

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `markowitz-ml-carteras-inversion.ipynb` en Google Colab, Jupyter o VS Code, o usa directamente la [liga de Colab](https://colab.research.google.com/drive/1mFF8xIFR8aaeIAxjeAHtza6P6Tj6Y4Kf?usp=sharing).
3. Si lo corres fuera de Colab, instala primero las dependencias con `pip install -r requirements.txt`.
4. Ejecuta todas las celdas en orden. Los precios se descargan en vivo desde yfinance, no requiere ningún archivo de datos local.
5. Para probar el pipeline con tu propia lista de activos, cambia la lista de tickers y el rango de fechas en la celda de descarga, y revisa cuántas filas sobreviven al cálculo de los indicadores técnicos antes de entrenar.

---
*Made with ❤️ by FuzzyFrog.AI*
