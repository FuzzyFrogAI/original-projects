# Robustez adversarial en la detección de cáncer de próstata

Clasificación de significancia histológica en imágenes de próstata con
**ResNet50** (transfer learning), puesta a prueba con un ataque adversario
**FGSM** y defendida con dos estrategias comparadas: entrenamiento con
datos mixtos (original + atacado) y fine-tuning.

Caso de estudio completo, con las decisiones de diseño explicadas:
https://fuzzyfrog.ai/es/ai-lab/proyectos/salud/deteccion-cancer-prostata-robustez-adversarial/

## El problema

Un modelo de diagnóstico por imagen puede tener accuracy alto en el set
de prueba y aun así ser vulnerable a perturbaciones imperceptibles al
ojo humano (ataques adversarios), capaces de cambiar su predicción sin
dejar rastro visual. Este notebook:

1. Entrena un modelo base (ResNet50) para clasificar significancia
   histológica (`significant` / `notsignificant`).
2. Lo ataca con FGSM para exponer la vulnerabilidad.
3. Construye y compara dos estrategias de defensa.
4. Mide la robustez con métricas del área (Adversarial Robustness
   Toolbox — ART), no solo con accuracy.

## Dataset

Imágenes histológicas de corte transversal de próstata (Kaggle):
https://www.kaggle.com/datasets/tgprostata/transverse-plane-prostate-dataset

Colócalo con esta estructura antes de correr el notebook:

```
Prostate Dataset/
├── train/
│   ├── significant/
│   └── notsignificant/
└── validation/
    ├── significant/
    └── notsignificant/
```

## Cómo correrlo

**Opción recomendada: Google Colab**

1. Sube `deteccion_cancer_prostata_robustez_adversarial.ipynb` a Colab
   (o ábrelo desde Google Drive).
2. Sube el dataset a tu Google Drive y ajusta la variable `ROOT_DIR` en
   la primera celda de código a la ruta donde lo dejaste.
3. Activa GPU: `Entorno de ejecución → Cambiar tipo de entorno de
   ejecución → GPU`.
4. Ejecuta las celdas en orden, de arriba hacia abajo. La primera celda
   instala `adversarial-robustness-toolbox`, que no viene preinstalado
   en Colab.

**Localmente (Jupyter)**

```bash
pip install tensorflow opencv-python-headless numpy pandas matplotlib \
            scikit-learn "adversarial-robustness-toolbox[tensorflow]" jupyter
jupyter notebook deteccion_cancer_prostata_robustez_adversarial.ipynb
```

## Qué hace cada sección del notebook

| Sección | Qué hace |
|---|---|
| 1. Setup y datos | Carga el dataset, define generadores de imágenes |
| 2. Modelo base | Entrena ResNet50 sin defensa (transfer learning) |
| 3. Ataque FGSM | Genera imágenes adversarias y mide la caída de accuracy |
| 4. Defensa adversarial | Entrena dos estrategias: datos mixtos y fine-tuning |
| 5. Evaluación de robustez | Compara accuracy, AUC-ROC y métricas ART entre los 3 modelos |
| 6. Demo rápido | Compara en vivo la predicción con/sin defensa sobre una imagen atacada |

## Resultados (se generan al correr el notebook)

El notebook guarda automáticamente `metricas_robustez_comparacion.csv`
con esta forma:

| Modelo | Accuracy (atacado) | AUC-ROC (atacado) | Loss sensitivity | Empirical robustness |
|---|---|---|---|---|
| sin_defensa | | | | |
| con_defensa | | | | |
| fine_tuning | | | | |

Los valores dependen de tu split y del epsilon usado (por default 0.05).

## Stack

Python · TensorFlow/Keras · OpenCV · Adversarial Robustness Toolbox (ART)
· scikit-learn

## Referencia

Adversarial attacks and adversarial robustness in computational
pathology. *Nature Communications* (2022).
https://www.nature.com/articles/s41467-022-33266-0

## Autor

Alan López — [FuzzyFrog.AI](https://fuzzyfrog.ai/es/)
