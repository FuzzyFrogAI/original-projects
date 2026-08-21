# Análisis de sentimientos con NLP — Reseñas turísticas del Perú

Clasificación de polaridad en reseñas de TripAdvisor sobre 25 sitios turísticos del Perú (uno por departamento), usando VADER con un léxico propio en español, comparación de 3 clasificadores y validación estadística contra la clasificación manual.

Basado en la tesis: *Modelo de procesamiento de lenguaje natural y análisis de sentimientos para la clasificación de reseñas de TripAdvisor de sitios turísticos del Perú* — Ignacio Melendrez Moreto, Universidad Nacional de Cajamarca, 2026.

## Resultados

| Modelo | Exactitud | Sensibilidad | Precisión | Puntaje F |
|---|---|---|---|---|
| Naïve Bayes | 0.6078 | 0.6181 | 0.6254 | 0.6110 |
| Random Forest | 0.6667 | 0.6954 | 0.7500 | 0.6657 |
| **LinearSVC (base)** | **0.6667** | 0.6558 | 0.6558 | **0.6540** |
| LinearSVC + RandomizedSearchCV | 0.6275 | — | — | 0.6102 |

Modelo final: **LinearSVC (base)**. La versión optimizada con `RandomizedSearchCV` no superó a la base — se reporta tal cual, sin forzar la narrativa de que optimizar siempre mejora.

### Validación contra el criterio humano (prueba Z pareada, n=110)

| Dimensión | Z | p-valor | Conclusión |
|---|---|---|---|
| Polaridad | 0.8936 | 0.3715 | Sin diferencia significativa vs. clasificación manual |
| Tiempo | -74.7452 | 0.0000 | 99% más rápido que el análisis manual (10,164 ms → 12.63 ms) |
| Relevancia | 6.5661 | ≈ 0 | Proporción de palabras clave significativamente > 0 |

## Datos

- **Corpus:** 623 reseñas, 25 sitios turísticos (uno por departamento del Perú), extraídas de páginas HTML de TripAdvisor.
- **Distribución original:** 285 positivas, 253 neutras, 85 negativas.
- **Balanceado:** submuestreo a 85 × 3 = 255 reseñas.
- **Test set:** 51 reseñas (20% de las 255 balanceadas).
- **Muestra de validación:** 110 reseñas con clasificación manual (pretest) para comparar contra el modelo (postest).

> Los datos crudos (páginas HTML descargadas, `PRETEST.csv`/`POSTTEST.csv` con la clasificación manual, y el shapefile de departamentos del Perú) no se incluyen en este repositorio por ser parte del material de tesis. El notebook documenta la metodología y el código completo.

## Pipeline

```
Reseñas HTML (TripAdvisor)
        │
        ▼
Preprocesamiento (limpieza + tokenización)
        │
        ├──► Polaridad: VADER + léxico en español (a priori, -4 a +4)
        └──► Relevancia: conteo de palabras clave turísticas
        │
        ▼
Balanceo de clases (submuestreo 85 × 3 = 255)
        │
        ▼
Vectorización TF-IDF
        │
        ▼
3 modelos comparados: Naïve Bayes · Random Forest · LinearSVC
        │
        ▼
Selección: LinearSVC (base)
        │
        ▼
Validación estadística: prueba Z pareada (pretest vs. postest, n=110)
        │
        ▼
Despliegue: mapa de sentimiento por departamento (geopandas + folium)
```

## Estructura del repositorio

```
.
├── README.md
├── requirements.txt
└── notebook_clasificacion_sentimientos_turismo_peru.ipynb
```

## Cómo usarlo

```bash
pip install -r requirements.txt
jupyter notebook notebook_clasificacion_sentimientos_turismo_peru.ipynb
```

El notebook requiere los datos privados descritos arriba para ejecutarse de punta a punta; se publica como referencia de metodología, decisiones de ingeniería y código.

## Aplicación real

El mapa de sentimiento por departamento, generado en el notebook con `geopandas` + `folium`, tiene una versión web sin esas dependencias (HTML/CSS/JS puro) lista para embeber en cualquier página: ver `mapa-interactivo.html` en el artículo del proyecto.

## Autor

Ignacio Melendrez Moreto — tesis, Universidad Nacional de Cajamarca.
Caso de estudio documentado por [Alan López](https://fuzzyfrog.ai/es/#about-temporary) — [ATLAS · FuzzyFrog.AI](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimientos-resenas-turismo-peru/).
