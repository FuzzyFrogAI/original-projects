# 🧪 Laboratorio: Matriz de KPIs de Negocio para un Modelo de Riesgo Crediticio - ATLAS FuzzyFrog.AI

**Objetivo:** aprender a evaluar un modelo de riesgo crediticio con KPIs de negocio propios de la industria, no solo con métricas técnicas de clasificación.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/matriz-kpis-negocio-modelo-riesgo-crediticio/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
matriz-kpis-negocio-modelo-riesgo-crediticio/
├── matriz-kpis-negocio-modelo-riesgo-crediticio.ipynb   # Notebook ejecutable, extremo a extremo
├── outputs/
│   └── dataset_sintetico_riesgo_crediticio.csv           # Dataset sintético de solicitudes de crédito
└── README.md                                             # Este archivo
```

## Enfoque de análisis

- 📊 **KS Score y Gini como métricas estándar de discriminación en scoring crediticio.** Ambas miden qué tan bien separa el modelo a buenos y malos pagadores, y son las métricas de referencia que usa la industria antes de considerar cualquier KPI operativo adicional. Referencia: Řezáč, M., & Řezáč, F. 2011. Measuring the Quality of Credit Scoring Models. Finance a úvěr, Czech Journal of Economics and Finance, 61(5), 486 a 507.
- 🌳 **Regresión logística sobre variables con criterio de dominio.** En scoring crediticio, un modelo interpretable con buenas variables construidas a mano suele igualar a técnicas más complejas, con la ventaja de ser auditable ante un comité de riesgo o un regulador. Referencia: Siddiqi, N. 2006. Credit Risk Scorecards, Developing and Implementing Intelligent Credit Scoring. Wiley.
- ⚠️ **El orden de las transformaciones en un pipeline de preprocesamiento importa.** Aplicar selección de variables basada en varianza después de estandarizar los datos anula el propósito de la técnica, porque el escalado ya normaliza la varianza de todas las columnas. Referencia: Kuhn, M., & Johnson, K. 2019. Feature Engineering and Selection, A Practical Approach for Predictive Models. CRC Press.
- 📈 **Ajustar el umbral de decisión, no solo el modelo.** El costo de un falso positivo y un falso negativo no es el mismo en un crédito, y el umbral de decisión debería reflejar esa diferencia de costo, en vez de dejarse en el valor por defecto de 0.5. Referencia: Elkan, C. 2001. The Foundations of Cost Sensitive Learning. Proceedings of the 17th International Joint Conference on Artificial Intelligence, IJCAI 2001.

## Metas

- Practicar la construcción de una matriz de KPIs de negocio con umbrales propios de una industria, más allá de precisión, recall o AUC.
- Aprender a detectar cuándo una técnica de selección de variables se aplicó en el orden equivocado y en la práctica no está haciendo nada.
- Entender por qué un modelo más complejo no siempre es mejor para el negocio, incluso cuando iguala o se acerca en desempeño técnico.
- Practicar el ajuste de un umbral de decisión en función de una restricción de negocio real, en vez de aceptar el valor por defecto de un clasificador.

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![seaborn](https://img.shields.io/badge/seaborn-visualizacion-4C72B0)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-006a87)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del caso](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/matriz-kpis-negocio-modelo-riesgo-crediticio/)
- Referencias citadas arriba en Enfoque de análisis
- [`matriz-kpis-negocio-modelo-riesgo-crediticio.ipynb`](./matriz-kpis-negocio-modelo-riesgo-crediticio.ipynb)

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `matriz-kpis-negocio-modelo-riesgo-crediticio.ipynb` en Jupyter, Google Colab o VS Code.
3. Ejecuta todas las celdas en orden. El dataset sintético se genera dentro del propio notebook y no requiere descargas externas.
4. Para adaptarlo a tu propio producto de crédito, reemplaza los umbrales de `kpis_targets` por los estándares reales de tu industria y de tu política de riesgo.
5. Ajusta `bad_rate_max` en la función de búsqueda de umbral según el límite de mora que tu negocio puede tolerar.

---
*Made with ❤️ by FuzzyFrog.AI*
