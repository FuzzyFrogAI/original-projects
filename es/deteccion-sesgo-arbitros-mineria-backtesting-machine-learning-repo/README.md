# 🧪 Laboratorio: Detección de Sesgo entre Árbitros de Minerales - FuzzyFrog.AI

**Objetivo:** aprender a diseñar una pregunta de negocio como una pregunta estadística contestable, y a validar un modelo con backtesting contra los métodos ya usados en la práctica.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/deteccion-sesgo-arbitros-mineria-backtesting-machine-learning/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
deteccion-sesgo-arbitros-mineria-backtesting-machine-learning/
├── deteccion-sesgo-arbitros-mineria-backtesting-machine-learning.ipynb   # Notebook: pruebas de hipótesis, modelos, clasificación y backtesting
├── outputs/
│   └── dataset_sintetico_arbitraje_minerales.csv                          # Dataset sintético con árbitros y clientes ficticios
└── README.md                                                               # Este archivo
```

## Enfoque de análisis

- 📐 **Prueba de hipótesis antes de modelar:** una prueba t de una muestra contra media cero, aplicada a la diferencia entre árbitro y vendedor, distingue una tendencia sistemática de una variación explicable por azar, tanto a nivel agregado como por cliente.
- 🌲 **Comparación de enfoques de modelado:** un modelo distinto por árbitro, evaluado contra siete algoritmos, para capturar el comportamiento específico de cada uno en lugar de mezclar todo en un solo modelo global.
- ⚖️ **Clasificación gana/pierde como pregunta complementaria:** un modelo de clasificación binaria responde directamente a quién favorece el resultado final, una pregunta de negocio a veces más útil que el valor exacto predicho.
- 🔁 **Backtesting contra los métodos ya usados:** el modelo se compara contra el promedio histórico de diferencia y una elección al azar entre comprador y vendedor, para demostrar con evidencia que aporta valor real.
- 📋 **Documentación honesta de la reducción del conjunto de datos:** filtrar para quedarse solo con los casos útiles redujo el conjunto original a una décima parte, una limitación real que se documenta en vez de ignorarse.

## Metas

- Traducir una pregunta de negocio ambigua en una pregunta estadística contestable con los datos disponibles.
- Aplicar pruebas de hipótesis para distinguir tendencia sistemática de variación aleatoria.
- Comparar múltiples algoritmos de regresión y de clasificación de forma organizada.
- Validar un modelo con backtesting contra los métodos ya usados en la práctica, no solo contra sí mismo.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-blue)
![scipy](https://img.shields.io/badge/scipy-pruebas%20de%20hip%C3%B3tesis-orange)
![scikit--learn](https://img.shields.io/badge/scikit--learn-regresi%C3%B3n%20%7C%20clasificaci%C3%B3n-yellow)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/deteccion-sesgo-arbitros-mineria-backtesting-machine-learning/)
- Notebook: `deteccion-sesgo-arbitros-mineria-backtesting-machine-learning.ipynb`

## Cómo usar

1. Clona este repositorio.
2. Abre `deteccion-sesgo-arbitros-mineria-backtesting-machine-learning.ipynb` en Jupyter o Google Colab.
3. Corre todas las celdas en orden, el dataset sintético se carga automáticamente desde `outputs/`.
4. Revisa la celda de la prueba de hipótesis por árbitro, y compárala con tu propio criterio antes de sacar conclusiones sobre sesgo con tus propios datos.

---

*Made with ❤️ by FuzzyFrog.AI*
