from sklearn.cluster import KMeans

import numpy as np


def cluster_img(img: np.ndarray, n: int) -> np.array:
    reshaped: np.ndarray = img.reshape((img.shape[0] * img.shape[1], 3))
    model: KMeans = KMeans(n_clusters=n)
    model.fit(reshaped)
    dominant_colors = model.cluster_centers_.astype(int)
    prediction = model.predict(reshaped)
    return np.array([dominant_colors[i] for i in prediction]).reshape(img.shape)
