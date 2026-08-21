"""
clustering_utils.py

Funciones reutilizables para comparar algoritmos de clustering bajo
las mismas métricas (SS between-cluster + error de clasificación LDA)
y para perfilar los clusters resultantes.

Uso típico:

    from src.clustering_utils import ss_between_cluster, error_clasificacion_lda, comparar_algoritmos

    resultados = comparar_algoritmos(X_scaled, k=4)
    print(resultados)
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn.neighbors import NearestNeighbors


def ss_between_cluster(X: np.ndarray, labels: np.ndarray, centers: np.ndarray) -> float:
    """Aproxima el % de varianza explicada por los clusters (SS between / SS total).

    Cuanto mayor, mejor separados están los clusters entre sí.
    """
    dists = cdist(X, centers)
    min_dist = dists.min(axis=1)
    return float((min_dist.sum() / dists.sum()) * 100)


def error_clasificacion_lda(X: np.ndarray, labels: np.ndarray) -> float:
    """Entrena un LDA sobre las etiquetas de cluster y devuelve el error de clasificación (%).

    Un error bajo indica que los clusters son consistentes y separables
    (un clasificador simple los puede distinguir), no solo que quedaron
    "cerca" según la métrica de distancia usada para formarlos.
    """
    if len(set(labels)) < 2:
        return float("nan")
    lda = LinearDiscriminantAnalysis()
    lda.fit(X, labels)
    pred = lda.predict(X)
    return float(100 * (1 - accuracy_score(labels, pred)))


def epsilon_por_knn(X: np.ndarray, k: int = 5) -> float:
    """Calcula un epsilon razonable para DBSCAN usando el codo de la distancia
    al k-ésimo vecino más cercano (heurística estándar)."""
    nbrs = NearestNeighbors(n_neighbors=k).fit(X)
    distancias, _ = nbrs.kneighbors(X)
    dist_k = np.sort(distancias[:, -1])
    diff = np.diff(dist_k)
    return float(dist_k[np.argmax(diff)])


def comparar_algoritmos(X: np.ndarray, k: int = 4, random_state: int = 123) -> pd.DataFrame:
    """Entrena K-Means, GMM y DBSCAN sobre X y devuelve una tabla comparativa.

    K-Medoids y Fuzzy C-Means requieren paquetes opcionales
    (scikit-learn-extra, fuzzy-c-means); se dejan fuera de esta función
    genérica para no forzar esas dependencias — ver el notebook
    01_segmentacion_operarios_clustering.ipynb para la comparación completa
    con los 4 algoritmos.
    """
    filas = []

    kmeans = KMeans(n_clusters=k, n_init=10, random_state=random_state)
    labels_kmeans = kmeans.fit_predict(X)
    filas.append({
        "algoritmo": "K-Means",
        "ss_between_cluster_%": ss_between_cluster(X, labels_kmeans, kmeans.cluster_centers_),
        "error_clasificacion_lda_%": error_clasificacion_lda(X, labels_kmeans),
        "n_clusters": k,
    })

    gmm = GaussianMixture(n_components=k, random_state=random_state, n_init=5)
    labels_gmm = gmm.fit_predict(X)
    filas.append({
        "algoritmo": "GMM",
        "ss_between_cluster_%": ss_between_cluster(X, labels_gmm, gmm.means_),
        "error_clasificacion_lda_%": error_clasificacion_lda(X, labels_gmm),
        "n_clusters": k,
    })

    eps = epsilon_por_knn(X)
    dbscan = DBSCAN(eps=eps, min_samples=10)
    labels_dbscan = dbscan.fit_predict(X)
    n_clusters_dbscan = len(set(labels_dbscan)) - (1 if -1 in labels_dbscan else 0)
    filas.append({
        "algoritmo": f"DBSCAN (eps={eps:.3f})",
        "ss_between_cluster_%": np.nan,
        "error_clasificacion_lda_%": error_clasificacion_lda(X, labels_dbscan) if n_clusters_dbscan > 1 else np.nan,
        "n_clusters": n_clusters_dbscan,
    })

    return pd.DataFrame(filas)


def perfilar_clusters(df: pd.DataFrame, cluster_col: str, agg_spec: dict) -> pd.DataFrame:
    """Genera una tabla de perfil por cluster a partir de un dict de agregaciones,
    p. ej. {'data_productividad_per': 'mean', 'data_Tedad': 'median'}.
    """
    return df.groupby(cluster_col).agg(agg_spec).round(1)
