# 🧪 Laboratorio: Optimización de carteras con LSTM, CAPM y Markowitz - ATLAS FuzzyFrog.AI

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20-FF6F00.svg)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ATLAS FuzzyFrog.AI](https://img.shields.io/badge/ATLAS-FuzzyFrog.AI-00b76c.svg)](https://fuzzyfrog.ai/es/)

**Aprende a no confiar en un modelo de Machine Learning hasta comprobar, fuera de muestra y contra la alternativa más simple, que de verdad mejora un portafolio de inversión.**

## Qué vas a aprender

Vas a practicar el criterio más importante de un proyecto cuantitativo: no confiar en un modelo hasta compararlo, fuera de muestra, contra la alternativa más simple que existe. En el camino tocas validación walk-forward con purga, CAPM como filtro por alfa, y por qué el objetivo del optimizador decide si tu pronóstico sirve o no.

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/) | [Todos los proyectos](https://fuzzyfrog.ai/es/ai-lab/proyectos/)

## Estructura del laboratorio

```
ml-portfolio-optimization-lstm-markowitz/
├── README.md                              ← este archivo
├── markowitz_ml_carteras_inversion.ipynb  ← notebook completo: datos, features, LSTM/GRU/Ridge/GB, CAPM, Markowitz, backtest
├── diagrama-solucion.svg                  ← diagrama del pipeline (fuente editable, mismo diseño que el artículo)
└── requirements.txt                       ← dependencias con versión fija
```

## Enfoque de análisis

- 🧠 **Pronóstico de rendimientos con LSTM/GRU/Ridge/Gradient Boosting**, comparados contra la media histórica y el paseo aleatorio con R² fuera de muestra y coeficiente de información — el modelo se compara siempre contra la alternativa que no aprende nada, no solo entre sí.
- 📉 **Filtro CAPM por alfa**: un activo solo entra al optimizador si su rendimiento pronosticado supera el mínimo que exige su riesgo de mercado. Sharpe, W. F. (1964). *Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk*. The Journal of Finance.
- 🧮 **Optimización de Markowitz con covarianza Ledoit-Wolf**, mínima volatilidad contra máximo Sharpe. Markowitz, H. (1952). *Portfolio Selection*. The Journal of Finance. Ledoit, O. & Wolf, M. (2004). *Honey, I Shrunk the Sample Covariance Matrix*. The Journal of Portfolio Management.
- 🔁 **Backtest walk-forward con purga y embargo**, medido fuera de muestra y con costos contra pesos iguales y el S&P 500. DeMiguel, V., Garlappi, L. & Uppal, R. (2009). *Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?*. The Review of Financial Studies.

## Explora las decisiones alternativas

Cada decisión de abajo se corrió con las dos opciones dentro del notebook. En el artículo puedes proponer tu propia alternativa antes de ver qué hubiera pasado:

- **¿Solo precio de cierre o con indicadores técnicos?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-lstm_indicadores)
- **¿Cuántas capas LSTM y cuántas unidades?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-lstm_arquitectura)
- **¿Incluir todos los activos en Markowitz o filtrar antes con CAPM?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-capm_filtro)
- **¿Minimizar volatilidad o maximizar el ratio de Sharpe?** → [Explorador de decisiones](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/#explorador-markowitz_objetivo)

## Metas

Al recorrer este repo vas a practicar:

- Diseñar un backtest walk-forward con purga y embargo que no deja fugarse ni un solo día de información.
- Construir features estacionarias que no crezcan sin límite, a diferencia de operar directo sobre el precio.
- Comparar modelos con la métrica que de verdad le importa a un portafolio: el coeficiente de información, no solo el error cuadrático.
- Decidir en qué punto del pipeline el pronóstico realmente llega a los pesos del portafolio, y en cuál se queda sin usarse.
- Leer un checklist metodológico con aserciones que corren de verdad, no solo texto narrativo, para descartar fugas y gaps antes de confiar en un resultado.

## Recursos

- **Plataforma**: [fuzzyfrog.ai](https://fuzzyfrog.ai/es/)
- **Artículo completo**: [Optimización de carteras con Machine Learning: LSTM, CAPM y Markowitz](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/markowitz-ml-carteras-inversion/)
- **Papers citados**: ver [Enfoque de análisis](#enfoque-de-análisis) arriba.
- **Notebook**: [`markowitz_ml_carteras_inversion.ipynb`](markowitz_ml_carteras_inversion.ipynb)

## Cómo usar

```bash
git clone https://github.com/FuzzyFrogAI/ml-portfolio-optimization-lstm-markowitz.git
cd ml-portfolio-optimization-lstm-markowitz
pip install -r requirements.txt
jupyter notebook markowitz_ml_carteras_inversion.ipynb
```

1. Clona el repositorio e instala las dependencias fijas de `requirements.txt`.
2. Abre `markowitz_ml_carteras_inversion.ipynb` (en Jupyter local o subiéndolo a Google Colab).
3. Córrelo de arriba a abajo. La celda 0 fija semilla, universo de activos y fechas; todo lo demás depende de esa configuración.
4. Al final, el notebook exporta `explorador_resultados.json`: son los números de cada decisión alternativa, la misma fuente que usa el Explorador de decisiones del artículo.

---

Made with 💚 by FuzzyFrog.AI
