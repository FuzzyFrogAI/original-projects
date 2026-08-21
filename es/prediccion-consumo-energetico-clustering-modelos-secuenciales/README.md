# 🧪 Laboratorio: Predicción de Consumo Energético con Clustering y Modelos Secuenciales - ATLAS FuzzyFrog.AI

**Aprende a segmentar el comportamiento de cientos de series antes de predecir, a elegir una arquitectura secuencial por simplicidad quien empata en desempeño, y a corregir el aplanamiento típico de un pronóstico autorregresivo de largo horizonte.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/prediccion-consumo-energetico-clustering-modelos-secuenciales/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
prediccion-consumo-energetico-clustering-modelos-secuenciales/
├── prediccion-consumo-energetico-clustering-modelos-secuenciales.ipynb   # Notebook principal: clustering, comparación de arquitecturas, pronóstico autorregresivo
├── outputs/
│   └── consumo_energetico_sintetico.csv   # Dataset sintético: 20 medidores, 3 arquetipos de perfil horario
└── README.md                               # Este archivo
```

## Enfoque de análisis

- 🧩 **Clustering de perfiles horarios como feature, no como análisis aparte.** El comportamiento de cada medidor se agrupa con K-Means, eligiendo el número de clústeres con el score de silueta, y ese clúster entra como variable del modelo secuencial. Referencia: Rousseeuw, P. J. (1987). *Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis*. Journal of Computational and Applied Mathematics, 20, 53–65. https://doi.org/10.1016/0377-0427(87)90125-7

- 🔄 **Codificación cíclica de la hora del día.** Evita que el modelo trate la medianoche y la 1 AM como valores lejanos entre sí. Referencia: *An Experimental Assessment of Treatments for Cyclical Data*. https://scholarworks.calstate.edu/downloads/pv63g5147

- ⚙️ **GRU elegida por simplicidad frente a LSTM cuando el desempeño empata.** Menos puertas internas, menos parámetros, mismo nivel de precisión. Referencia: Cho, K., et al. (2014). *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation*. https://arxiv.org/abs/1406.1078

- 🎲 **Ruido controlado para corregir el sesgo de un pronóstico autorregresivo.** Cuando un modelo se retroalimenta con sus propias predicciones, los errores se acumulan y la señal tiende a converger a un valor promedio; inyectar variabilidad controlada mitiga ese problema. Referencia: Bengio, S., Vinyals, O., Jaitly, N., & Shazeer, N. (2015). *Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks*. Advances in Neural Information Processing Systems (NeurIPS). https://arxiv.org/abs/1506.03099

## Metas

- Practicar clustering de series de tiempo por su perfil de comportamiento, antes de modelar
- Comparar arquitecturas secuenciales (RNN, LSTM, GRU, CNN-LSTM) con una metodología consistente
- Construir un pronóstico autorregresivo de largo horizonte y entender por qué necesita ajustes
- Reconocer las limitaciones de un pronóstico de largo plazo, incluso corregido

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-TensorFlow%2FKeras-FF6F00)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + comparación de arquitecturas): https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/prediccion-consumo-energetico-clustering-modelos-secuenciales/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook y dataset de ejercicios: `prediccion-consumo-energetico-clustering-modelos-secuenciales.ipynb` y `outputs/consumo_energetico_sintetico.csv`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `prediccion-consumo-energetico-clustering-modelos-secuenciales.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset sintético se carga automáticamente desde `outputs/consumo_energetico_sintetico.csv`.
4. Para probar el pipeline con tus propias lecturas, respeta las columnas (`id`, `ts`, `consumo`) y vuelve a correr desde la sección de modelado; el clustering, la ventana deslizante y la comparación de arquitecturas se recalculan automáticamente.

---

*Made with ❤️ by FuzzyFrog.AI*
