import numpy as np


def partition(img: np.ndarray) -> np.array:
    return np.array([[0] * 3 if sum(pixel) / 3. < 128 else [255] * 3 for pixel in
                     img.reshape(img.shape[0] * img.shape[1], 3)]).reshape(img.shape)
