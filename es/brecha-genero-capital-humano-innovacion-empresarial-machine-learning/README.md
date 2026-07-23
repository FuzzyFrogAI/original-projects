# 🧪 Laboratorio: Brecha de Género en el Capital Humano y la Innovación Empresarial - ATLAS FuzzyFrog.AI

**Aprende a medir con machine learning cuánto pesa la brecha de género frente a otros factores (inversión, financiamiento) en la capacidad de innovación de una empresa.**

## Enlaces rápidos

[Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocio/brecha-genero-capital-humano-innovacion-empresarial-machine-learning/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
brecha-genero-capital-humano-innovacion-empresarial-machine-learning/
├── brecha-genero-capital-humano-innovacion-empresarial-machine-learning.ipynb   # Notebook: carga, EDA, 4 hipótesis y hallazgos
├── data/
│   ├── df_manufactura.csv   # Microdatos EDIT (DANE), sector manufactura — descarga aparte
│   └── df_servicios.csv     # Microdatos EDIT (DANE), sector servicios — descarga aparte
└── README.md
```

## Enfoque de análisis

- 🎯 **Suma ponderada en vez de índice compuesto.** La capacidad de innovación se construyó como `0.6·innovación_producto_servicio + 0.4·innovación_proceso`, en vez de un índice de seis factores normalizados con pesos arbitrarios. Referencia de por qué la simplicidad suele generalizar mejor cuando no hay evidencia empírica para justificar pesos complejos: Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
- ⚖️ **Diferencias relativas para medir equidad, no conteos absolutos.** `diferencia_puestos` y `diferencia_educacion` aíslan la equidad de género del tamaño de la empresa. Referencia: Torchia, M., Calabrò, A., & Huse, M. (2011). Women directors on corporate boards: From tokenism to critical mass. *Journal of Business Ethics, 102*(2), 299–317.
- 🌲 **XGBoost sobre regresión lineal para capturar interacciones no lineales** entre inversión, financiamiento y género. Referencia: Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. *Proceedings of the 22nd ACM SIGKDD*.
- 🔮 **Red neuronal usada para simular escenarios, no solo para predecir.** Una vez entrenada, se le presentan casos hipotéticos (más equidad de género) para comparar contra el caso base. Referencia: Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.

## Metas

- Practicar la construcción de una métrica objetivo propia cuando la fuente de datos no la provee directamente.
- Aprender a separar una pregunta compleja en varias hipótesis, cada una con su propio modelo, en vez de forzar un solo modelo a responder todo.
- Ver un ejemplo real de cuándo una red neuronal se usa para simular escenarios de política, no solo para predecir un valor.
- Entender por qué reportar una limitación real de los datos (variable de barreras con poca variación) es parte del análisis, no un defecto que se esconde.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Regresión%20%2B%20Clasificación-EB0028)
![scikit--learn](https://img.shields.io/badge/scikit--learn-KMeans-F7931E?logo=scikitlearn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Red%20Neuronal-D00000?logo=keras&logoColor=white)
![Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocio/brecha-genero-capital-humano-innovacion-empresarial-machine-learning/)
- Papers citados en "Enfoque de análisis" arriba
- `brecha-genero-capital-humano-innovacion-empresarial-machine-learning.ipynb` (notebook principal)

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Descarga los microdatos EDIT correspondientes desde [microdatos.dane.gov.co](https://microdatos.dane.gov.co/index.php/catalog/MICRODATOS) (sector manufactura y sector servicios) y colócalos en `data/df_manufactura.csv` y `data/df_servicios.csv`.
3. Abre `brecha-genero-capital-humano-innovacion-empresarial-machine-learning.ipynb` en Jupyter o Google Colab.
4. Corre las celdas en orden: carga de datos → EDA → construcción de `capacidad_de_innovacion` → las cuatro hipótesis (H1 a H4).
5. Para probar la simulación de escenarios de H4, modifica los valores de `puestos_mujeres` y `educacion_mujeres` en la celda de simulación y vuelve a correrla.

---
*Made with ❤️ by FuzzyFrog.AI*
