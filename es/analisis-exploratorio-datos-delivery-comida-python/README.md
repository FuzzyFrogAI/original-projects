# 🧪 Laboratorio: Análisis Exploratorio de Datos de un Negocio de Delivery de Comida - FuzzyFrog.AI

**Aprende a validar cada hallazgo contra los datos antes de convertirlo en recomendación de negocio, sin necesitar ningún modelo predictivo.**

🔗 Enlaces rápidos: [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-exploratorio-datos-delivery-comida-python/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```plaintext
analisis-exploratorio-datos-delivery-comida-python/
├── README.md                                                  ← este archivo
├── analisis-exploratorio-datos-delivery-comida-python.ipynb    ← notebook completo, ejecutable en Colab
└── dataset/
    ├── foodhub_order.csv                                       ← dataset público, 1,898 pedidos
    ├── eda_foodhub_overview.png                                ← distribuciones univariadas
    └── eda_foodhub_bivariado.png                                ← relaciones bivariadas
```

## Enfoque de análisis

- 🔍 **Chequeo de calidad más allá de los nulos.** Un `.isnull().sum()` en cero no significa datos limpios: la columna de calificación mezcla texto ("Not given") y números, un patrón común que rompe cálculos si se convierte sin filtrar primero. Referencia: [McKinney, W. (2022). *Python for Data Analysis*, 3ra edición, O'Reilly — capítulo de limpieza y preparación de datos.](https://wesmckinney.com/book/)
- 📏 **Reglas de negocio con límites explícitos.** Toda regla de negocio en texto tiene casos frontera no decididos (¿qué pasa exactamente en $20.00?); decidirlos y documentarlos en el código evita que el resultado dependa de un supuesto silencioso.
- 📊 **Validación antes de recomendación.** Cada hallazgo se contrasta contra su distribución completa antes de convertirse en una recomendación, no solo contra un resumen agregado — así se encontró la ausencia total de calificaciones de 1 y 2 estrellas, un patrón que ningún resumen estadístico habría mostrado por sí solo.

## Metas

- Practicar el chequeo de calidad de datos más allá de la detección de nulos explícitos.
- Aprender a traducir reglas de negocio ambiguas en texto a condiciones exactas de código.
- Practicar análisis univariado y bivariado con pandas, matplotlib y seaborn.
- Entender por qué cada recomendación de negocio necesita evidencia específica, no una lectura superficial de los datos.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualizacion-3776AB)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter%2FColab-F37626?logo=jupyter&logoColor=white)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
- [Artículo completo del proyecto](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-exploratorio-datos-delivery-comida-python/)
- Referencia citada en Enfoque de análisis (ver arriba)
- Notebook: `analisis-exploratorio-datos-delivery-comida-python.ipynb`

## Cómo usar

1. Clona el repositorio: `git clone https://github.com/FuzzyFrogAI/original-projects.git`
2. Abre `analisis-exploratorio-datos-delivery-comida-python.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden — usan el dataset incluido en `dataset/foodhub_order.csv`.
4. Para adaptar el análisis a tu propio negocio, reemplaza el dataset conservando las mismas columnas, y ajusta los límites de las reglas de negocio (comisiones, criterios de promoción) a tus valores reales.

---

*Made with ❤️ by FuzzyFrog.AI*
