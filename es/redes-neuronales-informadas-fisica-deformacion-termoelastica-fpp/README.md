# 🧪 Laboratorio: Redes Neuronales Informadas por Física para Deformación Termoelástica - ATLAS FuzzyFrog.AI

**Aprende a diseñar una validación experimental que no sea circular, cuando tus datos de entrenamiento y tu término de regularización física vienen de la misma ecuación que quieres poner a prueba.**

🔗 Plataforma: https://fuzzyfrog.ai/es/ | 📄 Artículo completo: https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/redes-neuronales-informadas-fisica-deformacion-termoelastica-fpp/ | 📁 Todos los proyectos: https://github.com/FuzzyFrogAI/original-projects

## Estructura del laboratorio

```
redes-neuronales-informadas-fisica-deformacion-termoelastica-fpp/
└── redes-neuronales-informadas-fisica-deformacion-termoelastica-fpp.ipynb   # Notebook principal: modelo analítico, surrogate, validación externa
```

## Enfoque de análisis

- 🎲 **Muestreo por hipercubo latino para el dataset sintético.** Cobertura uniforme del espacio de parámetros con baja correlación entre variables, en vez de una malla regular o muestreo aleatorio simple. Referencia: McKay, M. D., Beckman, R. J., & Conover, W. J. (1979). *A Comparison of Three Methods for Selecting Values of Input Variables in the Analysis of Output from a Computer Code*. Technometrics, 21(2), 239–245. https://doi.org/10.1080/00401706.1979.10489755

- 🔬 **Teoría de placas de Kirchhoff-Love como fuente de datos de entrenamiento.** La solución cerrada de la ecuación de placa reemplaza a la simulación de elemento finito como generador de datos físicamente consistentes. Referencia: Leissa, A. W. (1969). *Vibration of Plates*. NASA SP-160, Scientific and Technical Information Division.

- 🌡️ **Número de Biot para descartar gradientes térmicos internos.** Antes de asumir que la placa se calienta de forma uniforme en su espesor, se verifica cuantitativamente que el régimen es térmicamente delgado. Referencia: Incropera, F. P., DeWitt, D. P., Bergman, T. L., & Lavine, A. S. *Fundamentals of Heat and Mass Transfer*. John Wiley & Sons.

- 📷 **Perfilometría de franjas como instrumento de calibración y validación.** Una técnica óptica de campo completo, sin contacto, capaz de resolver desplazamientos a escala micrométrica sobre la superficie de la placa. Referencia: Zuo, C., Feng, S., Huang, L., Tao, T., Yin, W., & Chen, Q. (2018). *Phase Shifting Algorithms for Fringe Projection Profilometry: A Review*. Optics and Lasers in Engineering, 109, 23–59. https://doi.org/10.1016/j.optlaseng.2018.04.019

## Metas

- Practicar la construcción de un dataset sintético físicamente consistente con muestreo por hipercubo latino
- Diseñar una comparación justa entre un modelo informado por física y baselines sin física del mismo tamaño
- Verificar con un análisis contrafactual que un punto de validación experimental no está contaminado por la calibración
- Aprender a documentar con honestidad dónde y por qué un modelo se queda corto, en vez de ocultarlo

## Insignias

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00)
![Framework](https://img.shields.io/badge/Framework-scikit--learn%20%7C%20SciPy-F7931E)
![Plataforma](https://img.shields.io/badge/FuzzyFrog.AI-ATLAS-00b76c)

## Recursos

- Plataforma: https://fuzzyfrog.ai/es/
- Artículo completo (diagrama interactivo + ecuaciones del modelo físico): https://fuzzyfrog.ai/es/ai-lab/proyectos/industria/redes-neuronales-informadas-fisica-deformacion-termoelastica-fpp/
- Papers citados arriba, en la sección Enfoque de análisis
- Notebook de ejercicios: `redes-neuronales-informadas-fisica-deformacion-termoelastica-fpp.ipynb`

## Cómo usar

1. Clona este repositorio o descarga la carpeta del proyecto.
2. Abre `redes-neuronales-informadas-fisica-deformacion-termoelastica-fpp.ipynb` en Google Colab o Jupyter.
3. Corre las celdas en orden; el dataset se genera analíticamente dentro del propio notebook, no requiere archivos externos.
4. Para probar con otras propiedades de material o geometría, modifica `E_esp`, `alpha_esp`, `L_esp` y `t_esp` en la sección de modelado y vuelve a correr desde ahí en adelante.

---

*Made with ❤️ by FuzzyFrog.AI*
