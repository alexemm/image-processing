import numpy as np


def dimm(x, brightness=0.6):
    return x * brightness


def lighten(x, brightness=1.4):
    return x * brightness if x * brightness < 255 else 255


def f(grid_size: int):
    for i in range(grid_size):
        if (i % 2) == 0 and (int(i / 8) % 2 == 0) or ((i % 2 != 0) and int(i / 8) % 2 != 0):
            yield i


def squarize(img: np.ndarray) -> np.ndarray:
    sqrWidth = np.ceil(np.sqrt(img.shape[0]*img.shape[1])).astype(int)
    im_resize = img.reshape((sqrWidth, sqrWidth, 3))
    return im_resize


def chess(img: np.ndarray, level: float = 0.8) -> np.array:
    square_img = squarize(img)
    #alpha = np.array([0.25, 0.25, 0.25]) * 4
    #channels = square_img.shape[2]
    max_size = square_img.shape[1]
    grid_size = int(max_size / 8)
    grids = [(x, y) for x in range(0, max_size, int(grid_size)) for y in range(0, max_size, int(grid_size))]
    dark_grid_edges = [grids[idx] for idx in f(grid_size)]
    dark_grids = [(range(dark_grid[0], dark_grid[0] + grid_size), range(dark_grid[1], dark_grid[1] + grid_size)) for
                  dark_grid in dark_grid_edges]
    new_img = np.zeros(img.shape, dtype='uint8')

    lighten_grade = 1 + level
    darken_grade = 1 - level
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            darken = False
            for dark_grid in dark_grids:
                if x in dark_grid[0] and y in dark_grid[1]:  # (x+y) % 2 == 0:
                    new_img[x, y] = dimm(img[x, y, 2], brightness=darken_grade)
                    darken = True
            if not darken:
                new_img[x, y] = lighten(img[x, y, 2], brightness=lighten_grade)
    return new_img
