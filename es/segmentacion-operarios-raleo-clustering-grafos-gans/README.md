# 🧪 Laboratorio: Segmentación de Operarios de Raleo y Otros Usos de Aprendizaje No Supervisado - FuzzyFrog.AI

**Objetivo:** aprender que el aprendizaje no supervisado no tiene una respuesta correcta contra la cual validar, así que la única forma de confiar en un resultado es comparar varios métodos y documentar hasta el que falla. Este laboratorio incluye tres cuadernos ejecutables, un dataset sintético y funciones reutilizables.

---

## 🚀 Enlaces rápidos
[🌐 FuzzyFrog.AI](https://fuzzyfrog.ai) | [📄 Artículo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/segmentacion-operarios-raleo-clustering-grafos-gans/) | [📁 Original Projects](../)

---

## 🏗 Estructura del laboratorio
```
/original-projects/segmentacion-operarios-raleo-clustering-grafos-gans
    README.md
    notebooks/
    raleo_base_clus_sintetico.csv
    src/
```
- `notebooks/`: tres cuadernos completos — segmentación de operarios (4 algoritmos de clustering), segmentación de imágenes por grafos, y generación de datos sintéticos con GAN.
- `raleo_base_clus_sintetico.csv`: dataset sintético (~900 registros) que imita la estructura y el comportamiento relativo de los datos reales de operarios. No contiene ningún dato real de cliente.
- `src/`: funciones reutilizables — comparación de algoritmos, perfilado de clusters y una función de inferencia rápida.

---

## 🔍 Enfoque de análisis
En este laboratorio vas a explorar tres decisiones clave detrás de convertir datos sin etiquetas en resultados accionables:

1. **Comparar algoritmos, no adoptar uno por default** 🧩
   - Entrenar K-Means, GMM, K-Medoids y Fuzzy C-Means sobre las mismas variables, y documentar también el intento fallido con DBSCAN como parte válida del análisis.

2. **Evaluación con doble métrica** ⚖️
   - Combinar SS-between-cluster (separación entre grupos) con el error de un LDA entrenado sobre las etiquetas de cluster (consistencia interna), en vez de confiar en un solo número.
   - Paper de referencia: [Cluster validity methods: part I](https://dl.acm.org/doi/10.1145/568574.568575)

3. **Aprendizaje no supervisado más allá del clustering tabular** 🔗
   - Segmentación de imágenes por grafos (SLIC + Normalized Cut + GrabCut) y generación de datos sintéticos con GANs para compensar la escasez de una clase minoritaria.
   - Paper de referencia: [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)

---

## 🎯 Metas
- Comparar varios algoritmos de clustering bajo las mismas métricas antes de elegir uno.
- Practicar la evaluación de clusters con más de un criterio (separación + consistencia).
- Explorar segmentación por grafos y generación de datos sintéticos con GANs como usos de aprendizaje no supervisado más allá del clustering.
- Construir una función de inferencia rápida para validar un segmento antes de construir una aplicación completa.

---

## 🛠 Insignias
![Python](https://img.shields.io/badge/python-3.10-blue)
![Notebook](https://img.shields.io/badge/notebook-jupyter-orange)
![scikit--learn](https://img.shields.io/badge/scikit--learn-clustering-yellowgreen)
![TensorFlow](https://img.shields.io/badge/tensorflow-GAN-red)
![Website](https://img.shields.io/badge/fuzzyfrog.ai-visitar-brightgreen)

---

## 📚 Recursos
- [FuzzyFrog.AI](https://fuzzyfrog.ai)
- Artículo completo con las decisiones de diseño: [Artículo](https://fuzzyfrog.ai/es/ai-lab/proyectos/mineria/segmentacion-operarios-raleo-clustering-grafos-gans/)
- Referencias y papers listados arriba
- Ejercicios en `notebooks/`

---

## ✨ Cómo usar
1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/original-projects.git
```
2. Instala dependencias: `pip install -r requirements.txt`
3. Abre los cuadernos de `notebooks/` en Jupyter o Google Colab y corre cada uno con los datos incluidos.
4. Prueba la función de inferencia rápida (`predecir_segmento`) al final del primer cuaderno con tus propios datos de entrada.

---

*Made with ❤️ by FuzzyFrog.AI*
