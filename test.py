from filtering_algs.chess import chess
from filtering_algs.k_means_filtering import cluster_img
from filtering_algs.contrast_partition import partition
from utils.img_tools import load_img, plot_img, save_img

import cv2 as cv


def test_kmeans(n: int = 2) -> None:
    dir = 'imgs/'
    img = 'Lenna_(test_image).png'
    img = load_img(dir + img, transparent=False)
    new_img = cluster_img(img, n)
    plot_img(new_img)
    save_img('new_imgs/test.png', new_img)


def test_partition() -> None:
    dir = 'imgs/'
    img = 'Lenna_(test_image).png'
    img = load_img(dir + img, transparent=False)
    new_img = partition(img)
    #plot_img(new_img)
    save_img('new_imgs/test2.png', new_img)


def test_chess() -> None:
    dir = 'imgs/'
    img = 'Lenna_(test_image).png'
    #img = 'chang.jpeg'
    img = load_img(dir + img, transparent=False)
    new_img = chess(img, 0.5)
    #plot_img(new_img)
    save_img('new_imgs/test3.png', new_img)


if __name__ == '__main__':
    #test_partition()
    test_chess()
