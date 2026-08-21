# Detección temprana de displasia de cadera (DDC) con ResNet50 y GANs

Clasificación de radiografías pélvicas anteroposteriores de infantes de 3 a 6 meses como
**DDC** (displasia del desarrollo de cadera) o **Normal**, combinando aumento de datos con
una GAN y transfer learning con ResNet50.

Caso de estudio completo, con diagrama interactivo del pipeline y demo del umbral de decisión:
**https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-displasia-cadera-resnet50-gan/**

> ⚠️ **Disclaimer médico.** Este repositorio es material educativo. El modelo es un sistema
> de *apoyo* diagnóstico entrenado sobre 354 sujetos de dos hospitales; no está validado
> clínicamente ni debe usarse para diagnosticar pacientes reales. Todo caso requiere
> confirmación de un especialista.

## Resultados

| Métrica | CNN baseline | ResNet50 (transfer learning + fine-tuning) |
| --- | --- | --- |
| Exactitud | 74.29% | 97.43% |
| Sensibilidad | 73.74% | 98.82% |
| Precisión | 75.43% | 96.00% |
| AUC-ROC | 0.74 | 0.97 |

## Pipeline

1. **Preprocesamiento** — resize 224×224, escala de grises, filtro Gaussiano 3×3, normalización [0,1].
2. **Exploración de separabilidad** — K-Means + PCA sobre características simples, para confirmar que había señal antes de comprometerse con una arquitectura.
3. **Aumento de datos con GAN** — generador/discriminador entrenados de forma adversarial, balancean el dataset real (120 DDC / 234 Normal) a 350 sujetos por clase con radiografías sintéticas.
4. **Baseline** — SVM, Árbol de Decisión y una CNN simple, como punto de comparación honesto.
5. **Modelo final** — ResNet50 preentrenado en ImageNet: cabeza nueva entrenada con el modelo base congelado, luego fine-tuning de las últimas 20 capas con un learning rate bajo.
6. **Evaluación** — exactitud, sensibilidad, precisión, matriz de confusión y curva ROC.

## Estructura del repositorio

```
.
├── README.md
├── requirements.txt
├── displasia_cadera_resnet50_gan.ipynb   # notebook limpio y comentado
├── data/                                 # no incluido — ver "Datos" abajo
│   ├── DDH/
│   └── Normal/
└── models/                               # modelos entrenados (.h5 / SavedModel), no incluidos
```

## Datos

El dataset original (354 sujetos: 120 DDC, 234 Normal) proviene de dos hospitales del norte
de Jordania, publicado en:

> Fraiwan, M., Al-Kofahi, N., Ibnian, A., & Hanatleh, O. (2022). Detection of developmental
> dysplasia of the hip in X-ray images using deep transfer learning. *BMC Medical Informatics
> and Decision Making*, 22(216). https://doi.org/10.1186/s12911-022-01957-9

Por restricciones de privacidad de datos médicos, las imágenes no se incluyen en este
repositorio. Coloca tus propias radiografías (o el dataset público citado arriba, si tienes
acceso) en `data/DDH/` y `data/Normal/` antes de correr el notebook.

## Cómo correrlo

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook displasia_cadera_resnet50_gan.ipynb
```

Se recomienda GPU para las secciones de entrenamiento de la GAN y de ResNet50 (Google Colab
con GPU gratuita es suficiente para reproducir los resultados).

## Referencia relacionada

Para el estado más amplio de la literatura en este campo:
[Artificial Intelligence to Detect Developmental Dysplasia of Hip: A Systematic Review](https://onlinelibrary.wiley.com/doi/10.1111/jpc.70172) (Bhavsar et al., 2025).

## Autor

[Alan López — FuzzyFrog.AI](https://fuzzyfrog.ai/es/#about-temporary)
Artículo del proyecto: https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/clasificacion-displasia-cadera-resnet50-gan/
