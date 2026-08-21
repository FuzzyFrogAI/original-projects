# Nota sobre los datos

Los datos originales de operarios de raleo (campaña agrícola, sede Piura) son propiedad de la empresa cliente y contienen información personal (edad, número de hijos, indicador de pobreza, historial crediticio) que no puede publicarse.

`raleo_base_clus_sintetico.csv` es un dataset **sintético**, generado con distribuciones estadísticas plausibles y del mismo esquema de columnas que el dataset real, para que:

- El proyecto sea completamente reproducible por cualquier persona.
- Los resultados de clustering, aunque no coincidirán en valores exactos con los del caso real, muestren el mismo comportamiento relativo entre algoritmos (K-Means vs. GMM vs. K-Medoids vs. Fuzzy C-Means vs. DBSCAN).
- No se exponga ningún dato personal identificable.

Si tienes tus propios datos reales (con permiso de uso), basta con reemplazar este CSV manteniendo las mismas columnas.
