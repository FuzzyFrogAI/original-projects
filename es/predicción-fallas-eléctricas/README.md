# 🧪 Laboratory: Electrical Grid Failure Classification - FuzzyFrog.AI

**Objective:** Learn how to combine tabular and free-text data into a single multimodal classifier when your target categories are noisy and imbalanced. This hands-on lab provides a runnable notebook, a synthetic dataset, and references to the underlying techniques.

---

## 🚀 Quick Links
[🌐 FuzzyFrog.AI](https://fuzzyfrog.ai) | [📄 Article](https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/clasificacion-fallas-red-electrica-texto-tabular-bert/) | [📁 Original Projects](../)

---

## 🏗 Laboratory Structure
```
/original-projects/electrical-grid-failure-classification
    README.md
    fallas_redes_electricas.ipynb
    fallas_red_electrica_sintetico.csv
    resources/
```
- `fallas_redes_electricas.ipynb`: full notebook — load, EDA, modeling (TabBERT), evaluation, and a quick inference function.
- `fallas_red_electrica_sintetico.csv`: reduced synthetic dataset (~650 records) mirroring the structure and class imbalance of the original project. Contains no real client data.
- `resources/`: architecture diagram and supporting material.

---

## 🔍 Analysis Focus
In this lab, you will explore three key decisions behind turning noisy, multimodal data into a working classifier:

1. **Category Grouping** 🧩
   - Collapse noisy, low-signal categories into classes with real business meaning before modeling.
   - Reference Paper: [A Survey on Data Preprocessing for Data Mining](https://arxiv.org/abs/2202.01593)

2. **Multimodal Fusion (Tabular + Text)** 🔗
   - Combine categorical/numerical embeddings with a BERT-based text embedding in a single architecture.
   - Reference Paper: [Multimodal Machine Learning: A Survey and Taxonomy](https://arxiv.org/abs/1705.09406)

3. **Class Imbalance Handling** ⚖️
   - Oversampling plus a class-weighted loss to keep minority classes learnable through training.
   - Reference Paper: [Learning from Imbalanced Data](https://ieeexplore.ieee.org/document/5128907)

---

## 🎯 Goals
- Identify when noisy categorical targets need regrouping before modeling.
- Practice fusing tabular and free-text data in one architecture.
- Learn to handle class imbalance beyond naive oversampling.
- Build a quick inference function to validate a model before building a full app.

---

## 🛠 Badges
![Python](https://img.shields.io/badge/python-3.10-blue)
![Notebook](https://img.shields.io/badge/notebook-jupyter-orange)
![PyTorch](https://img.shields.io/badge/pytorch-deep%20learning-red)
![Website](https://img.shields.io/badge/atlas--ai--thesis--lab-visit-brightgreen)

---

## 📚 Resources
- [FuzzyFrog.AI](https://fuzzyfrog.ai)
- Full write-up with design decisions: [Article](https://fuzzyfrog.ai/es/ai-lab/proyectos/energia/clasificacion-fallas-red-electrica-texto-tabular-bert/)
- References and papers listed above
- Exercises in `fallas_redes_electricas.ipynb`

---

## ✨ How to Use
1. Clone the repository:
```bash
git clone https://github.com/yourusername/original-projects.git
```
2. Open `fallas_redes_electricas.ipynb` in Jupyter or Google Colab.
3. Run the notebook end to end with the included synthetic dataset.
4. Try the quick inference function at the end with your own inputs.

---

*Made with ❤️ by FuzzyFrog.AI*
