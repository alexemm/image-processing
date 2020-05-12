import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def load_img(file: str, transparent: bool = True) -> np.ndarray:
    """
    Loads image file as 3D-Matrix
    :param file: relative path to file
    :param transparent: Load transparent image or not
    :return: image file as Numpy 3D-Matrix
    """
    mode: int = cv.IMREAD_COLOR
    if transparent:
        mode: int = cv.IMREAD_UNCHANGED
    return cv.imread(file)


def save_img(name: str, img: np.ndarray) -> None:
    """
    Saves numpy array as image file
    :param name: Name of file
    :param img: Image representation as a numpy array
    :param dir: directory to destination folder
    :return: None
    """
    cv.imwrite(name, img)


def plot_img(img: np.array) -> None:
    cv.imshow("", img.astype(np.uint8))
    cv.waitKey()

