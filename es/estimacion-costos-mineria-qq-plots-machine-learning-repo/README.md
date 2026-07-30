# 🧪 Laboratorio: Estimación de Costos en Minería con Q-Q Plots - FuzzyFrog.AI

**Objetivo:** aprender a validar las distribuciones de los datos con Q-Q plots antes de entrenar un modelo, y comparar múltiples modelos de regresión con evidencia objetiva.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/estimacion-costos-mineria-qq-plots-machine-learning/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
estimacion-costos-mineria-qq-plots-machine-learning/
├── estimacion-costos-mineria-qq-plots-machine-learning.ipynb   # Notebook: limpieza, Q-Q plots, selección de variables y comparación de modelos
├── outputs/
│   └── dataset_sintetico_costos_mineria.csv                    # Dataset sintético de operación minera diaria
└── README.md                                                    # Este archivo
```

## Enfoque de análisis

- 📐 **Validación de distribuciones antes de modelar:** cada variable se compara contra tres distribuciones candidatas, normal, gamma y lognormal, usando Q-Q plots, antes de decidir si necesita transformarse o si un modelo lineal es razonable para ella.
- 🌲 **Selección de variables por importancia, no por intuición:** un bosque aleatorio mide cuánto aporta cada variable a la predicción antes de comprometerse con un modelo final.
- ⚖️ **Comparación objetiva de seis modelos de regresión:** desde regresión lineal hasta un perceptrón multicapa, con métricas comparadas en entrenamiento y en prueba, en vez de quedarse con el primer modelo que funciona.
- 📋 **Documentación honesta de un comportamiento inusual en los datos:** la humedad se comporta como una variable casi categórica, algo que solo se hizo evidente al revisar su Q-Q plot, y se documenta como tal en vez de forzar una distribución continua sobre ella.

## Metas

- Entender qué es un Q-Q plot y cómo interpretarlo.
- Validar los supuestos distribucionales de los datos antes de confiar en un modelo de regresión.
- Medir la importancia relativa de variables con un bosque aleatorio.
- Comparar múltiples modelos de regresión con criterios objetivos de error.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-blue)
![scikit--learn](https://img.shields.io/badge/scikit--learn-regresi%C3%B3n-orange)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-yellow)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/estimacion-costos-mineria-qq-plots-machine-learning/)
- Notebook: `estimacion-costos-mineria-qq-plots-machine-learning.ipynb`

## Cómo usar

1. Clona este repositorio.
2. Abre `estimacion-costos-mineria-qq-plots-machine-learning.ipynb` en Jupyter o Google Colab.
3. Corre todas las celdas en orden, el dataset sintético se carga automáticamente desde `outputs/`.
4. Revisa la sección de Q-Q plots y compárala con tus propios datos antes de asumir que un modelo lineal es adecuado para tu caso.

---

*Made with ❤️ by FuzzyFrog.AI*
