# Segmentación de operarios y otros usos de aprendizaje no supervisado

Proyecto de dos módulos (folds) construidos sobre la misma pregunta de fondo — encontrar estructura en datos sin etiquetas — aplicados a dos dominios distintos.

## Fold 1 — Segmentación de operarios de raleo (clustering tabular)

Comparación objetiva de 4 algoritmos de clustering sobre datos reales (anonimizados/sintéticos para publicación) de operarios de raleo de uva de una campaña agrícola en Piura:

- **K-Means** — particional, clusters esféricos
- **Modelo de Mezcla Gaussiana (GMM)** — probabilístico, admite formas elípticas y solapamiento
- **K-Medoids** — robusto a outliers, usa observaciones reales como centro
- **Fuzzy C-Means** — pertenencia parcial (difusa) a más de un cluster

Se documenta también el intento con **DBSCAN**, que no logró encontrar estructura interpretable en estos datos tabulares de escalas mixtas — un resultado negativo relevante para justificar la elección final.

Cada algoritmo se evalúa con dos criterios independientes:
1. **SS between-cluster** — separación entre grupos
2. **Error de clasificación de un LDA** entrenado sobre las etiquetas de cluster — consistencia/predictibilidad de los grupos

## Fold 2 — Otros usos de aprendizaje no supervisado (imágenes)

Dos técnicas de aprendizaje no supervisado sobre imágenes, reencuadradas hacia un caso de **inspección visual de calidad**:

- **Segmentación por grafos**: superpíxeles (SLIC) → grafo de adyacencia de regiones (RAG) → corte normalizado (Normalized Cut), más **GrabCut** para segmentación semiautomática fondo/objeto.
- **Generación de contenido con GANs**: red generativa adversaria entrenada para producir ejemplos sintéticos de una clase minoritaria (defecto), balanceando el dataset de entrenamiento de un clasificador de calidad.

## Estructura del repositorio

```
segmentacion-operarios-raleo-aprendizaje-no-supervisado/
├── README.md
├── requirements.txt
├── data/
│   ├── raleo_base_clus_sintetico.csv     # datos sintéticos de operarios (estructura real, valores no reales)
│   └── NOTA_CONFIDENCIALIDAD.md
├── notebooks/
│   ├── 01_segmentacion_operarios_clustering.ipynb
│   ├── 02_segmentacion_grafos_ncut_grabcut.ipynb
│   └── 03_generacion_gan_sinteticos.ipynb
└── src/
    ├── clustering_utils.py     # comparación de algoritmos, perfilado de clusters
    └── gan_utils.py            # generador/discriminador reutilizables
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo correrlo

1. `notebooks/01_segmentacion_operarios_clustering.ipynb` — usa `data/raleo_base_clus_sintetico.csv`, no requiere GPU.
2. `notebooks/02_segmentacion_grafos_ncut_grabcut.ipynb` — descarga imágenes de ejemplo públicas (scikit-image + una imagen de muestra), no requiere GPU.
3. `notebooks/03_generacion_gan_sinteticos.ipynb` — usa MNIST como proxy de "clase minoritaria de defecto"; recomendable con GPU, pero corre en CPU (más lento).

## Nota sobre los datos

Los datos reales de operarios de la campaña de raleo son confidenciales del cliente. `data/raleo_base_clus_sintetico.csv` es un dataset sintético que preserva la estructura de columnas y rangos plausibles de valores, generado para que el proyecto sea reproducible sin exponer información real — ver `data/NOTA_CONFIDENCIALIDAD.md`.

## Licencia

MIT — libre de usar y adaptar citando la fuente.

## Autor

Alan López — [fuzzyfrog.ai](https://fuzzyfrog.ai/es/)
