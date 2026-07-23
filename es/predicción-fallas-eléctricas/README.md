# 🧪 Laboratorio: Clasificación de Fallas en Redes Eléctricas - FuzzyFrog.AI

**Objetivo:** aprender a combinar datos tabulares y texto libre en un solo clasificador multimodal, cuando las categorías objetivo son ruidosas y están desbalanceadas. Este laboratorio incluye un cuaderno ejecutable, un dataset sintético y referencias a las técnicas utilizadas.

---

## 🚀 Enlaces rápidos
[🌐 FuzzyFrog.AI](https://fuzzyfrog.ai) | [📄 Artículo](https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/clasificacion-fallas-red-electrica-texto-tabular-bert/) | [📁 Original Projects](../)

---

## 🏗 Estructura del laboratorio
```
/original-projects/clasificacion-fallas-red-electrica
    README.md
    fallas_redes_electricas.ipynb
    fallas_red_electrica_sintetico.csv
    resources/
```
- `fallas_redes_electricas.ipynb`: cuaderno completo — carga, EDA, modelado (TabBERT), evaluación y una función de inferencia rápida.
- `fallas_red_electrica_sintetico.csv`: dataset sintético reducido (~650 registros) que imita la estructura y el desbalance de clases del proyecto original. No contiene ningún dato real de cliente.
- `resources/`: diagrama de arquitectura y material de apoyo.

---

## 🔍 Enfoque de análisis
En este laboratorio vas a explorar tres decisiones clave detrás de convertir datos ruidosos y multimodales en un clasificador funcional:

1. **Agrupación de categorías** 🧩
   - Colapsar categorías ruidosas y de bajo aporte en clases con significado real de negocio antes de modelar.
   - Paper de referencia: [A Survey on Data Preprocessing for Data Mining](https://arxiv.org/abs/2202.01593)

2. **Fusión multimodal (tabular + texto)** 🔗
   - Combinar embeddings de categóricas/numéricas con un embedding de texto basado en BERT, dentro de una sola arquitectura.
   - Paper de referencia: [Multimodal Machine Learning: A Survey and Taxonomy](https://arxiv.org/abs/1705.09406)

3. **Manejo de desbalance de clases** ⚖️
   - Oversampling más un loss ponderado por clase, para que las clases minoritarias sigan siendo aprendibles durante el entrenamiento.
   - Paper de referencia: [Learning from Imbalanced Data](https://ieeexplore.ieee.org/document/5128907)

---

## 🎯 Metas
- Identificar cuándo una variable objetivo ruidosa necesita reagruparse antes de modelar.
- Practicar la fusión de datos tabulares y texto libre en una sola arquitectura.
- Aprender a manejar el desbalance de clases más allá del oversampling ingenuo.
- Construir una función de inferencia rápida para validar un modelo antes de construir una aplicación completa.

---

## 🛠 Insignias
![Python](https://img.shields.io/badge/python-3.10-blue)
![Notebook](https://img.shields.io/badge/notebook-jupyter-orange)
![PyTorch](https://img.shields.io/badge/pytorch-deep%20learning-red)
![Website](https://img.shields.io/badge/fuzzyfrog.ai-visitar-brightgreen)

---

## 📚 Recursos
- [FuzzyFrog.AI](https://fuzzyfrog.ai)
- Artículo completo con las decisiones de diseño: [Artículo](https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/clasificacion-fallas-red-electrica-texto-tabular-bert/)
- Referencias y papers listados arriba
- Ejercicios en `fallas_redes_electricas.ipynb`

---

## ✨ Cómo usar
1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/original-projects.git
```
2. Abre `fallas_redes_electricas.ipynb` en Jupyter o Google Colab.
3. Corre el cuaderno completo con el dataset sintético incluido.
4. Prueba la función de inferencia rápida al final con tus propios datos de entrada.

---

*Made with ❤️ by FuzzyFrog.AI*
