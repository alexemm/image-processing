import numpy as np
import cv2


def dimm(x, brightness=0.6):
    return x * brightness


def lighten(x, brightness=1.4):
    return x * brightness if x * brightness < 255 else 255


# Load an color image in grayscale
img = cv2.imread('lena512color.tiff', cv2.IMREAD_COLOR)
rbg_img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

print('loaded img')

max_size = 512
grid_size = int(max_size/8)


def f(grid_size=grid_size):
    #for i in range()
    for i in range(grid_size):
        if ((i % 2) == 0 and (int(i / 8) % 2 == 0) or ((i % 2 != 0) and int(i / 8) % 2 != 0)):
            yield i

alpha = np.array([0.25, 0.25, 0.25]) * 4
channels = 3
grids = [(x, y) for x in range(0, max_size , int(grid_size)) for y in range(0, max_size , int(grid_size))]
#grids = [rbg_img[x: x + int(grid_size)][y: y + int(grid_size)] for x in range(0, 512, int(grid_size)) for y in range(0, 512, int(grid_size))]

dark_grid_edges = [grids[idx]for idx in f()]
dark_grids = [(range(dark_grid[0], dark_grid[0] + grid_size), range(dark_grid[1], dark_grid[1] + grid_size)) for dark_grid in dark_grid_edges]


#img_grids = [dimm(img[x, y]) if (x+y) % 2 == 0 else lighten(img[x, y]) for y in range(img.shape[0]) for x in range(img.shape[1])]
new_img = np.zeros(img.shape, dtype='uint8')
level = 0.8
lighten_grade = 1 + level
darken_grade = 1 - level
#import pdb; pdb.set_trace();
for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        darken = False

        for dark_grid in dark_grids:

            if x in dark_grid[0] and y in dark_grid[1]:#(x+y) % 2 == 0:

                new_img[x, y] = dimm(img[x, y, 2], brightness=darken_grade)#[:, :, 2])#(alpha.dot(img[x, y])/channels)
                darken = True
        if not darken:
            new_img[x, y] = lighten(img[x, y, 2], brightness=lighten_grade)#[:, :, 2])#(alpha.dot(img[x, y])/channels)
print('created new img...\nNow show')
#h, w = new_img.shape
#newer_img = cv2.cvtColor(new_img, cv2.COLOR_GRAY2BGR)
cv2.imshow('image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
