<h1 align="center">Mantenimiento Predictivo del Desgaste de Studs en Rodillo HPGR</h1>

<p align="center"><strong>Entender el fenómeno físico antes de modelar hace que un modelo simple y explicable venza a modelos más complejos.</strong></p>

<p align="center">
  <a href="https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/mantenimiento-predictivo-desgaste-studs-rodillo-hpgr/">Artículo completo (ES)</a> ·
  <a href="https://fuzzyfrog.ai/en/ai-lab/proyectos/mining/predictive-maintenance-hpgr-roll-stud-wear/">Full article (EN)</a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-1.x-F7931E?logo=scikitlearn&logoColor=white">
  <img alt="pandas" src="https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white">
  <img alt="Dataset" src="https://img.shields.io/badge/dataset-sint%C3%A9tico-00b76c">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
</p>

---

## Enlaces rápidos

- [Artículo (ES)](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/mantenimiento-predictivo-desgaste-studs-rodillo-hpgr/)
- [Article (EN)](https://fuzzyfrog.ai/en/ai-lab/proyectos/mining/predictive-maintenance-hpgr-roll-stud-wear/)
- [Notebook ejecutable](outputs/mantenimiento_predictivo_desgaste_hpgr.ipynb)
- [Dataset sintético](outputs/hpgr_stud_wear_synthetic.csv)

## Árbol de archivos

```
.
├── README.md
├── mantenimiento-predictivo-desgaste-studs-rodillo-hpgr.html
├── mantenimiento-predictivo-desgaste-studs-rodillo-hpgr-aside-menu.html
├── mantenimiento-predictivo-desgaste-studs-rodillo-hpgr-diagrama-interactivo.html
├── predictive-maintenance-hpgr-roll-stud-wear.html
├── predictive-maintenance-hpgr-roll-stud-wear-aside-menu.html
├── predictive-maintenance-hpgr-roll-stud-wear-diagrama-interactivo.html
└── outputs/
    ├── generar_dataset_sintetico.py
    ├── hpgr_stud_wear_synthetic.csv
    └── mantenimiento_predictivo_desgaste_hpgr.ipynb
```

## Decisiones técnicas

**1. Ingeniería de características basada en el mecanismo físico, no en las columnas crudas.** El desgaste de un stud en un HPGR sigue un mecanismo abrasivo documentado en la literatura de procesamiento de minerales (Kazerani Nejad & Sam, 2016, *"The wear pattern in high pressure grinding rolls"*, DOI: [10.1080/03719553.2016.1263059](https://doi.org/10.1080/03719553.2016.1263059)). En vez de entrenar directamente con horómetro, periodo y tonelaje crudos, se construyeron ratios e interacciones que traducen ese mecanismo a variables: eficiencia de uso del tiempo, tonelaje por hora y tonelaje logarítmico. Esta decisión precede a cualquier elección de algoritmo.

**2. Comparación de modelos con validación cruzada, no con una sola partición.** Se entrenaron cinco modelos (Regresión Lineal, Árbol de Decisión, Random Forest, SVR, Gradient Boosting) y se evaluaron con validación cruzada de 5 particiones. La Regresión Lineal obtuvo el menor RMSE promedio (1.99 mm), por delante de Random Forest (2.93 mm) y Gradient Boosting (3.04 mm). Elegir con una sola partición de prueba habría sido más rápido, pero menos confiable.

**3. Preferir el modelo más simple cuando el desempeño es comparable.** El modelo final es la Regresión Lineal, no por ser el de menor error absoluto en abstracto, sino porque su ventaja de simplicidad e interpretabilidad (coeficientes explicables directamente a mantenimiento) pesa más que una diferencia de desempeño pequeña frente a modelos más opacos.

**4. Dataset sintético con nota explícita, no datos reales de la operación.** Las mediciones de desgaste de un HPGR son datos propietarios de una operación minera y no se pueden publicar. El dataset sintético (`outputs/hpgr_stud_wear_synthetic.csv`) replica la estructura, los tipos de dato y la relación física entre horómetro, periodo, tonelaje y desgaste, en un tamaño reducido, generado con `outputs/generar_dataset_sintetico.py`.

## Metas

- [x] Entender el mecanismo físico de desgaste antes de construir features
- [x] Ingeniería de características informada por el fenómeno
- [x] Comparación honesta de 5 modelos con validación cruzada
- [x] Interpretación de coeficientes del modelo final
- [x] Dataset sintético demostrativo, sin datos reales de ninguna operación
- [ ] Extensión a series temporales para predecir la fecha exacta de reemplazo (fuera del alcance de este artículo)

## Recursos

- Kazerani Nejad, R. & Sam, A. (2016). *The wear pattern in high pressure grinding rolls*. Mineral Processing and Extractive Metallurgy. DOI: [10.1080/03719553.2016.1263059](https://doi.org/10.1080/03719553.2016.1263059)
- [scikit-learn: model evaluation](https://scikit-learn.org/stable/modules/cross_validation.html)

## Cómo usar

```bash
git clone https://github.com/FuzzyFrogAI/original-projects.git
cd original-projects/es/mantenimiento-predictivo-desgaste-studs-rodillo-hpgr
pip install -r requirements.txt   # pandas, numpy, scikit-learn, matplotlib, seaborn, nbformat
python outputs/generar_dataset_sintetico.py
jupyter notebook outputs/mantenimiento_predictivo_desgaste_hpgr.ipynb
```

---

<p align="center">Escrito por <a href="https://fuzzyfrog.ai/es/#about-temporary">Alan López</a> · <a href="https://fuzzyfrog.ai/es/">FuzzyFrog.AI</a></p>
