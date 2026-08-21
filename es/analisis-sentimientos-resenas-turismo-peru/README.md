# 🧪 Laboratorio: Análisis de Sentimientos en Reseñas Turísticas del Perú - FuzzyFrog.AI

**Objetivo:** aprender a construir un clasificador de sentimiento en español cuando no existe un léxico confiable para el dominio, y a validar ese modelo contra el criterio humano con una prueba estadística en vez de conformarte con la exactitud. Este laboratorio incluye un cuaderno ejecutable, un dataset sintético y referencias a las técnicas utilizadas.

---

## 🚀 Enlaces rápidos
[🌐 FuzzyFrog.AI](https://fuzzyfrog.ai) | [📄 Artículo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimientos-resenas-turismo-peru/) | [📁 Original Projects](../)

---

## 🏗 Estructura del laboratorio
```
/original-projects/analisis-sentimientos-turismo-peru
    README.md
    sentimientos_turismo_peru.ipynb
    resenas_turismo_peru_sintetico.csv
    resources/
```
- `sentimientos_turismo_peru.ipynb`: cuaderno completo — extracción, preprocesamiento (VADER + léxico en español), balanceo de clases, modelado (3 clasificadores comparados), validación estadística y despliegue en mapa por departamento.
- `resenas_turismo_peru_sintetico.csv`: dataset sintético reducido que imita la estructura y el desbalance de clases del proyecto original (25 sitios turísticos, 3 clases de polaridad). No contiene ningún dato real de usuario.
- `resources/`: diagrama de arquitectura y material de apoyo.

---

## 🔍 Enfoque de análisis
En este laboratorio vas a explorar tres decisiones clave detrás de convertir reseñas de texto libre en español en un clasificador de sentimiento confiable:

1. **Léxico de sentimiento a la medida del idioma y del dominio** 🧩
   - VADER no trae un léxico confiable para español: construir uno propio, en la misma escala -4 a +4 del original, con reglas de negaciones e intensificadores, antes de clasificar nada.

2. **Comparación justa de modelos sobre la misma entrada** 🔗
   - Evaluar varios algoritmos (Naïve Bayes, Random Forest, LinearSVC) sobre el mismo TF-IDF y el mismo conjunto de prueba, y reportar cuando optimizar hiperparámetros no mejora el resultado.
   - Paper de referencia: [VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text](https://ojs.aaai.org/index.php/ICWSM/article/view/14550)

3. **Validación estadística contra el criterio humano** ⚖️
   - No basta con reportar exactitud: una prueba Z pareada entre clasificación manual y automática demuestra si el modelo realmente sustituye al criterio humano, o solo se le parece.
   - Paper de referencia: [Statistical Comparisons of Classifiers over Multiple Data Sets](https://www.jmlr.org/papers/v7/demsar06a.html)

---

## 🎯 Metas
- Identificar cuándo un dominio y un idioma necesitan un léxico propio antes de aplicar una herramienta de sentimiento genérica.
- Practicar la comparación honesta de varios clasificadores sobre la misma entrada.
- Aprender a validar un modelo contra un criterio humano con estadística, no solo con una métrica aislada.
- Convertir el resultado de un notebook en un artefacto desplegable: un mapa interactivo por departamento.

---

## 🛠 Insignias
![Python](https://img.shields.io/badge/python-3.10-blue)
![Notebook](https://img.shields.io/badge/notebook-jupyter-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-modelado-red)
![Website](https://img.shields.io/badge/fuzzyfrog.ai-visitar-brightgreen)

---

## 📚 Recursos
- [FuzzyFrog.AI](https://fuzzyfrog.ai)
- Artículo completo con las decisiones de diseño: [Artículo](https://fuzzyfrog.ai/es/ai-lab/proyectos/negocios/analisis-sentimientos-resenas-turismo-peru/)
- Referencias y papers listados arriba
- Ejercicios en `sentimientos_turismo_peru.ipynb`

---

## ✨ Cómo usar
1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/original-projects.git
```
2. Abre `sentimientos_turismo_peru.ipynb` en Jupyter o Google Colab.
3. Corre el cuaderno completo con el dataset sintético incluido.
4. Prueba la clasificación de una reseña propia al final del cuaderno.

---

*Made with ❤️ by FuzzyFrog.AI*
