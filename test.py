from filtering_algs.k_means_filtering import cluster_img
from utils.img_tools import load_img, plot_img, save_img

import cv2 as cv


def test_kmeans(n: int = 2) -> None:
    dir = 'imgs/'
    img = 'Lenna_(test_image).png'
    img = load_img(dir + img, transparent=False)
    for i in range(4, 5):
        new_img = cluster_img(img, i)
        plot_img(new_img)
    save_img('new_imgs/test.png', new_img)


if __name__ == '__main__':
    test_kmeans()
