# 🧪 Laboratorio: Predicción de la Curva de Fragmentación en Voladura - FuzzyFrog.AI

**Aprende a justificar un criterio de limpieza de outliers con un requisito de negocio real, y por qué la validación cruzada puede invertir por completo qué modelo parece ganar.**

🔗 Enlaces rápidos: [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/prediccion-curva-fragmentacion-voladura-ml/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```plaintext
prediccion-curva-fragmentacion-voladura-ml/
├── README.md                                              ← este archivo
├── prediccion-curva-fragmentacion-voladura-ml.ipynb        ← notebook completo, ejecutable en Colab
└── dataset/
    ├── dataset_fragmentacion_sintetico.csv                 ← dataset sintético (relaciones Kuz-Ram)
    ├── comparacion_modelos_fragmentacion.csv                ← RMSE por modelo y target (validación cruzada)
    ├── sintonizacion_svr.csv                                ← RMSE antes/después de sintonizar el SVR
    └── curvas_fragmentacion_ejemplo.png                     ← curvas real vs predicha, 4 muestras
```

## Enfoque de análisis

- 🎯 **Corte de outliers ligado a un requisito de confianza, no a una convención.** Se usa un corte de 0.2 desviaciones estándar, mucho más estricto que el 2-3 sigma habitual, justificado explícitamente por la necesidad de que el modelo caiga dentro de un intervalo de confianza del 95% dada la alta dispersión natural de los datos de voladura.
- 📊 **Validación cruzada como estándar mínimo, nunca in-sample.** Comparar los 3 modelos in-sample llevó a una conclusión opuesta (Random Forest "ganando" en todos los targets) a la que dio la validación cruzada de 5 pliegues (SVR ganando en 9 de 12). Referencia: [Kohavi, R. (1995). *A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection*.](https://www.ijcai.org/Proceedings/95-2/Papers/016.pdf)
- 🌍 **Modelo Kuz-Ram como base física del dataset sintético.** El dataset de demostración no es ruido aleatorio: sigue las relaciones del modelo Kuz-Ram, el estándar de la industria para modelar fragmentación de voladura. Referencia: [Cunningham, C.V.B. (1987). *Fragmentation estimations and the Kuz-Ram model — four years on*.](https://www.researchgate.net/publication/292918658)

## Metas

- Practicar la justificación de decisiones de preprocesamiento (outliers, escalado) con criterios de negocio explícitos, no defaults.
- Aprender por qué evaluar in-sample sobreestima modelos flexibles como Random Forest.
- Practicar el benchmarking correcto de modelos de regresión con validación cruzada y sintonización de hiperparámetros vía `RandomizedSearchCV`.
- Entender cuándo la sintonización de hiperparámetros no mejora el resultado, y por qué eso no invalida el proceso.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-SVR%2FRF%2FLinReg-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter%2FColab-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/prediccion-curva-fragmentacion-voladura-ml/)
- Papers citados en Enfoque de análisis (ver arriba)
- Notebook: `prediccion-curva-fragmentacion-voladura-ml.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Abre `prediccion-curva-fragmentacion-voladura-ml.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden — usan el dataset sintético incluido en `dataset/`.
4. Para usar tus propios datos de voladura, reemplaza la celda de carga de datos siguiendo las instrucciones comentadas en el notebook, y ajusta el corte de outliers al nivel de confianza que tu proyecto requiera.

---

*Made with ❤️ by FuzzyFrog.AI*
