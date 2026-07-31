# 🧪 Laboratorio: Predicción de Rendimientos de Bonos del Tesoro de EE.UU. - ATLAS FuzzyFrog.AI

**Aprende a combinar selección de variables, corrección de estacionariedad e ingeniería de indicadores técnicos con modelos secuenciales para pronosticar una curva de rendimientos completa, sin depender de un modelo de lenguaje.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-rendimientos-bonos-tesoro-eeuu-indicadores-tecnicos/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
prediccion-rendimientos-bonos-tesoro-eeuu-indicadores-tecnicos/
├── prediccion-rendimientos-bonos-tesoro-eeuu-indicadores-tecnicos.ipynb   # Notebook principal: EDA, indicadores técnicos, modelos por plazo
├── outputs/
│   └── rendimientos_bonos_sintetico.csv   # Dataset sintético: curva de rendimientos (8 plazos) + indicadores macro
└── README.md                               # Este archivo
```

## Enfoque de análisis

- 📊 **Selección de variables por información mutua.** En vez de usar las ~20 variables macro completas, se mide la información mutua de cada una contra los rendimientos y se conservan solo las más informativas, reduciendo ruido y colinealidad antes de modelar. Referencia: Battiti, R. (1994). *Using mutual information for selecting features in supervised neural net learning*. IEEE Transactions on Neural Networks, 5(4), 537–550. https://doi.org/10.1109/72.298224

- 📉 **Prueba de estacionariedad (ADF) + diferenciación.** Los rendimientos no son estacionarios en niveles, así que se prueban con Dickey-Fuller Aumentada y se diferencian antes de entrar a cualquier modelo, para no inflar artificialmente el desempeño reportado. Referencia: Dickey, D. A., & Fuller, W. A. (1979). *Distribution of the Estimators for Autoregressive Time Series With a Unit Root*. Journal of the American Statistical Association, 74(366), 427–431. https://doi.org/10.2307/2286348

- 🔁 **Indicadores técnicos como features.** SMA, Bandas de Bollinger, RSI y autocorrelación lag-1 se calculan sobre la serie diferenciada, para darle al modelo una señal de momentum y volatilidad que el nivel crudo no tiene. Referencia: *LSTM Deep Learning Based Stock Price Prediction with Bollinger Band, RSI, MACD, and OHLC Features*. International Journal of Intelligent Systems and Applications in Engineering. https://ijisae.org/index.php/IJISAE/article/view/5396

- 🧠 **GRU por plazo en vez de un solo modelo para toda la curva.** Cada uno de los 8 plazos se entrena por separado porque el tramo corto y el tramo largo de la curva responden a dinámicas distintas. Referencia: Cho, K., et al. (2014). *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation*. https://arxiv.org/abs/1406.1078

## Metas

- Practicar selección de variables con información mutua sobre series económicas correlacionadas
- Aplicar pruebas de estacionariedad (ADF) y diferenciación antes de modelar series de tiempo financieras
- Construir indicadores técnicos (SMA, Bollinger, RSI, autocorrelación) como ingeniería de características explícita
- Entrenar y evaluar modelos secuenciales (RNN/LSTM/GRU) por plazo, con métricas de error estándar (MSE, MAE, R2)

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-TensorFlow%2FKeras-FF6F00)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + ecuaciones de cada indicador): https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/prediccion-rendimientos-bonos-tesoro-eeuu-indicadores-tecnicos/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `prediccion-rendimientos-bonos-tesoro-eeuu-indicadores-tecnicos.ipynb` y `outputs/rendimientos_bonos_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `prediccion-rendimientos-bonos-tesoro-eeuu-indicadores-tecnicos.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/rendimientos_bonos_sintetico.csv`.
4. Para probar el pipeline con otro plazo de la curva, cambia el nombre de la columna objetivo en la celda de modelado (por ejemplo, de `USGG3M Index` a `USGG5YR Index`) y vuelve a correr esa celda en adelante.

---

*Made with ❤️ by FuzzyFrog.AI*
