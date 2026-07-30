# 🧪 Laboratorio: Keras-RL, DQN y Arquitecturas de Aprendizaje por Refuerzo - FuzzyFrog.AI

**Objetivo:** aprender a construir y entrenar un agente DQN desde cero, y entender cómo han evolucionado las arquitecturas de redes neuronales para aprendizaje por refuerzo.

**Enlaces rápidos:** [Plataforma](https://fuzzyfrog.ai/es/) | [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/keras-rl-dqn-arquitecturas-aplicaciones-aprendizaje-refuerzo/) | [Carpeta general de proyectos](https://github.com/FuzzyFrogAI/original-projects)

## Estructura del laboratorio

```
keras-rl-dqn-arquitecturas-aplicaciones-aprendizaje-refuerzo/
├── keras-rl-dqn-arquitecturas-aplicaciones-aprendizaje-refuerzo.ipynb   # Notebook: entorno, preprocesamiento, red DQN, entrenamiento y evaluación
└── README.md                                                            # Este archivo
```

## Enfoque de análisis

- 🕹️ **Red convolucional para estimar el valor de cada acción a partir de una imagen:** tres capas convolucionales seguidas de una capa densa, la misma arquitectura de base que demostró desempeño a nivel humano en decenas de juegos de Atari. Referencia: Mnih, V., et al. (2015). Human-level control through deep reinforcement learning. Nature, 518(7540), 529-533.
- ♟️ **El mismo principio escalado a un dominio mucho más complejo:** redes neuronales profundas combinadas con búsqueda, superando a jugadores de élite en el juego de Go. Referencia: Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search. Nature, 529(7587), 484-489.
- 🔥 **Aprendizaje por refuerzo aplicado a control físico en tiempo real:** un agente aprendiendo a controlar el plasma dentro de un reactor de fusión nuclear, muy lejos de un videojuego pero construido sobre la misma idea central. Referencia: Degrave, J., et al. (2022). Magnetic control of tokamak plasmas through deep reinforcement learning. Nature, 602(7897), 414-419.
- ⚙️ **Ajuste fino documentado, no solo el resultado final:** el notebook conserva las iteraciones de hiperparámetros que llevaron a la versión final del agente, incluyendo por qué se ajustó cada uno.

## Metas

- Construir una red convolucional para estimar valores de acción a partir de frames de video.
- Entrenar un agente DQN completo: memoria de repetición, política de exploración decreciente y red objetivo.
- Ajustar hiperparámetros de forma iterativa, documentando el porqué de cada cambio.
- Entender la evolución de las arquitecturas de aprendizaje por refuerzo desde DQN hasta los enfoques actuales.

## Insignias

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![Keras--RL](https://img.shields.io/badge/Keras--RL-DQN-yellow)
![FuzzyFrog.AI](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- [Plataforma](https://fuzzyfrog.ai/es/)
- [Artículo completo](https://fuzzyfrog.ai/es/ai-lab/proyectos/educacion/keras-rl-dqn-arquitecturas-aplicaciones-aprendizaje-refuerzo/)
- Referencias citadas en "Enfoque de análisis" (ver arriba)
- Notebook: `keras-rl-dqn-arquitecturas-aplicaciones-aprendizaje-refuerzo.ipynb`

## Cómo usar

1. Clona este repositorio.
2. Crea un entorno virtual local, este proyecto depende de versiones específicas de Gym, TensorFlow y Keras-RL que no siempre son compatibles con notebooks alojados en la nube.
3. Abre `keras-rl-dqn-arquitecturas-aplicaciones-aprendizaje-refuerzo.ipynb` y corre las celdas en orden, cada bloque de entrenamiento se ejecuta como script independiente.
4. Prueba el agente ya entrenado ajustando `episodes` en la función `test()` para correr más partidas de evaluación.

---

*Made with ❤️ by FuzzyFrog.AI*
