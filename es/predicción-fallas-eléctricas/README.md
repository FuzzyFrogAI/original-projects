# Predicción de causas de falla en una red de distribución eléctrica

Clasificación multimodal (datos tabulares + texto libre) de la causa de una falla eléctrica, combinando embeddings tabulares con un modelo de lenguaje (DistilBERT) sobre comentarios de campo.

**Artículo completo con el contexto, el diseño y las decisiones de este proyecto:** *(liga a la plataforma — sección Fallas en redes eléctricas)*

## Contenido de este repositorio

- `fallas_redes_electricas.ipynb` — cuaderno completo: carga de datos, EDA, modelado (TabBERT), evaluación y función de inferencia rápida.
- `fallas_red_electrica_sintetico.csv` — dataset sintético reducido (~650 registros) que imita la estructura y el desbalance de clases del proyecto original. No contiene ningún dato real de cliente.

## Nota sobre los datos

Por confidencialidad, este repositorio usa datos sintéticos generados para fines demostrativos. La arquitectura, las decisiones de ingeniería y los resultados descritos en el artículo corresponden al proyecto real; los datos no.

## Resumen técnico

- **Problema:** clasificar la causa de una interrupción eléctrica en 3 clases (`Natural`, `Interna/Accidente`, `Otros`), a partir de datos tabulares (circuito, municipio, duración) y un comentario de texto libre del operador.
- **Enfoque:** arquitectura TabBERT — embeddings de categóricas + numérica escalada, concatenados con el embedding `[CLS]` de DistilBERT sobre el comentario, seguido de una capa densa con dropout.
- **Manejo de desbalance:** oversampling de clases + loss ponderado por clase durante el entrenamiento.
- **Resultado (con datos reales del proyecto original):** ~80% de exactitud en la clasificación de 3 clases.

## ¿Tienes un proyecto similar?

Puedo ayudarte a diseñar un enfoque parecido para tu tesis, tu trabajo o tu emprendimiento. Más información en la plataforma: *(liga a la plataforma)*
