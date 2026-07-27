# Posts de LinkedIn — Clasificación de Riesgo de Salud Mental con NLP y Embeddings
### Español · 7 posts · autocontenidos

---

## Post 1
**Hook:** Value Promise · **Formato:** Educativo (Prueba/autoridad → Problema → Explicación → Pasos) · **Gancho emocional:** FOMO
**Keyword:** machine learning

Vas a aprender cómo diseñar un clasificador de texto para salud mental que quepa en un presupuesto de nivel gratuito, sin sacrificar calidad en la representación del lenguaje.

En un proyecto reciente de machine learning aplicado a salud mental universitaria, el reto no era conseguir el modelo más potente disponible. Era conseguir uno que fuera bueno y que costara casi nada de mantener.

🧠 Lo que hace falta para lograrlo:
🔹 Representar el texto con embeddings de un modelo preentrenado, no con bolsa de palabras clásica
🔹 Elegir un clasificador simple y rápido de servir, como una regresión logística
🔹 Definir con claridad qué decide el modelo y qué decide siempre una persona

El resultado fue un sistema que prioriza qué casos revisar primero, nunca que decide un diagnóstico. Ese límite se definió desde el diseño, no se agregó después.

🔗 El paso a paso completo, con el código y las decisiones explicadas, está en el artículo: [ESPACIO PARA LIGA DEL ARTÍCULO]

Si estás por iniciar un proyecto de machine learning con presupuesto limitado, yo te ayudo a diseñarlo desde cero.

---

## Post 2
**Hook:** Controversial Statement · **Formato:** Confianza (Historia → Lección → Aplicación) · **Gancho emocional:** Curiosity Gap
**Keyword:** inteligencia artificial

Un modelo de inteligencia artificial nunca debería decidir si alguien necesita ayuda psicológica urgente. Y precisamente por eso este proyecto funcionó.

La historia empezó con una pregunta incómoda: si construíamos un clasificador de riesgo de salud mental a partir de texto libre, ¿hasta dónde le dejábamos decidir?

📖 La decisión que tomamos desde el inicio fue clara: el modelo solo prioriza, nunca diagnostica. La salida es un nivel de urgencia de revisión, y la decisión clínica final siempre queda en manos de un profesional de salud mental.

🎯 La aplicación de esta lección va más allá de este proyecto: cualquier sistema de inteligencia artificial que toque un dominio sensible necesita ese límite definido desde el diseño, no como un parche ético agregado al final.

🔗 Cómo se construyó ese límite en el sistema, en el artículo completo: [ESPACIO PARA LIGA DEL ARTÍCULO]

Si tu proyecto toca un dominio sensible y no sabes cómo trazar ese límite, yo te ayudo a diseñarlo.

---

## Post 3
**Hook:** Proof Hook · **Formato:** Conversión (Resultado → Situación inicial → Qué cambió → Resultado específico → Siguientes pasos) · **Gancho emocional:** FOMO
**Keyword:** proyectos de machine learning

52.681 textos etiquetados, un modelo ligero, y un clasificador desplegable en una función serverless de bajo costo. Así se construyó este proyecto de machine learning aplicado a salud mental.

📌 Situación inicial: no había un dataset propio de respuestas reales anotado por profesionales para entrenar un modelo desde cero, y el presupuesto de infraestructura era casi nulo.

🔧 Qué cambió: se adoptó un dataset público de texto sobre salud mental, y se representó ese texto con embeddings de un modelo preentrenado en vez de bolsa de palabras clásica, combinado con un clasificador ligero.

📈 Resultado específico: un pipeline completo, de texto libre a nivel de urgencia, corriendo dentro del presupuesto de una arquitectura serverless de nivel gratuito.

Siguiente paso si tienes un proyecto similar: no asumas que necesitas el modelo más grande, define primero el presupuesto real de infraestructura y diseña hacia atrás desde ahí.

🔗 Todo el detalle técnico, en el artículo: [ESPACIO PARA LIGA DEL ARTÍCULO]

¿Tu proyecto de machine learning tiene restricciones reales de presupuesto? Yo te ayudo a diseñar la solución que sí quepa en ellas.

---

## Post 4
**Hook:** Fear Hook · **Formato:** Educativo · **Gancho emocional:** Curiosity Gap
**Keyword:** deep learning

Un modelo de deep learning entrenado sobre un dataset desbalanceado puede parecer excelente en el papel, y fallar exactamente en los casos que más importa detectar bien.

Esto es lo que hay que vigilar en cualquier proyecto de clasificación de riesgo, especialmente en salud mental, donde las categorías más urgentes suelen tener muchos menos ejemplos disponibles.

📌 El problema en números simples:
▪️ Las categorías más comunes dominan el dataset
▪️ Las categorías clínicamente más urgentes representan una fracción mínima de los ejemplos
▪️ La exactitud global puede verse bien mientras el modelo comete más errores justo ahí

🛠️ Cómo se aborda:
1️⃣ Ponderar el entrenamiento por clase, para que las categorías raras pesen más
2️⃣ Reportar el desempeño por clase, no solo la exactitud general
3️⃣ Revisar con especial cuidado la categoría de mayor urgencia antes de confiar en el modelo

🔗 Cómo se aplicó esto en el proyecto completo, en el artículo: [ESPACIO PARA LIGA DEL ARTÍCULO]

Si tu proyecto de deep learning tiene ese mismo riesgo de desbalance en las clases importantes, yo te ayudo a diseñar la validación correcta.

---

## Post 5
**Hook:** Unexplained Contrast · **Formato:** Confianza · **Gancho emocional:** FOMO
**Keyword:** aprendizaje de inteligencia artificial

El modelo más nuevo no ganó. El modelo más barato sí.

Así de simple fue la decisión detrás de este proyecto de aprendizaje de inteligencia artificial aplicado a un cuestionario de salud mental universitario.

📖 La historia: existía la opción de ajustar un modelo de lenguaje completo, del tipo que hoy domina las conversaciones sobre inteligencia artificial. También existía la opción de usar embeddings preentrenados junto con un clasificador simple.

La primera opción no cabía en el presupuesto de una función serverless de nivel gratuito. La segunda sí, y con un desempeño más que suficiente para el objetivo real del proyecto.

🎯 La aplicación: la pregunta correcta casi nunca es "cuál es el modelo más avanzado que existe", sino "cuál es el modelo más simple que resuelve bien este problema dentro de mis restricciones reales".

🔗 La comparación completa entre ambas opciones, en el artículo: [ESPACIO PARA LIGA DEL ARTÍCULO]

Si tu proyecto de aprendizaje de inteligencia artificial tiene restricciones de presupuesto que no sabes cómo resolver, yo te ayudo a diseñarlo.

---

## Post 6
**Hook:** Emotional Agreement · **Formato:** Educativo · **Gancho emocional:** Curiosity Gap
**Keyword:** inteligencia artificial generativa

A veces sientes que hablar de inteligencia artificial generativa es hablar solo de modelos enormes y conversaciones automáticas. Y a veces la decisión más valiosa es exactamente la contraria.

En este proyecto de salud mental, la pregunta no fue qué tan grande podía ser el modelo, sino qué tan bien podía representar el significado de un texto sin volverse imposible de sostener económicamente.

🧠 Lo que se decidió:
🔹 Usar embeddings de un modelo de lenguaje preentrenado, una pieza de la misma familia de avances detrás del boom actual de inteligencia artificial generativa
🔹 Mantener el clasificador final simple, ligero y explicable
🔹 Reservar la complejidad para donde realmente aporta valor, la representación del lenguaje, no el clasificador final

📖 La lección de fondo: aprovechar los avances recientes de inteligencia artificial generativa no siempre significa usar el modelo más grande de punta a punta. A veces significa tomar solo la pieza que aporta valor real a tu problema específico.

🔗 Cómo se combinó esto en el pipeline completo, en el artículo: [ESPACIO PARA LIGA DEL ARTÍCULO]

Si sientes que no sabes por dónde empezar a aplicar esto en tu propio proyecto, yo te ayudo a diseñarlo.

---

## Post 7
**Hook:** Combo Hook (Proof + Value Promise) · **Formato:** Conversión · **Gancho emocional:** FOMO
**Keyword:** proyectos de machine learning + inteligencia artificial

Un dataset público de más de 52.000 textos, un modelo ligero desplegado en infraestructura de bajo costo, y un límite ético definido desde el diseño. Eso es lo que puedes lograr cuando conviertes una tesis en un proyecto de inteligencia artificial completo, no solo en un experimento de código.

Este fue el cierre de un proyecto que combinó procesamiento de lenguaje natural, criterio de ingeniería sobre presupuesto real, y una definición clara de hasta dónde llega la automatización en un dominio sensible.

🏆 Lo que vas a encontrar si sigues este mismo enfoque en tus propios proyectos de machine learning:
✅ Cómo elegir entre un modelo grande y uno ligero según tus restricciones reales, no según la moda
✅ Cómo manejar un dataset desbalanceado sin engañarte con la exactitud global
✅ Cómo trazar, desde el diseño, el límite entre lo que decide un modelo y lo que debe decidir siempre una persona

La parte más valiosa no fue el código, fue el criterio para decidir qué tan lejos dejar llegar la automatización antes de que un humano tuviera que tomar el control.

🔗 El artículo completo, con el diagrama interactivo del pipeline y el notebook ejecutable: [ESPACIO PARA LIGA DEL ARTÍCULO]

Si tienes un proyecto que necesita ese mismo criterio, de ingeniería y de límites claros, yo te ayudo a diseñarlo de principio a fin.
