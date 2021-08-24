import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import util


def function(src, Proportion):
    Noise_img = src
    Noise_num = int(Proportion*src.shape[0]*src.shape[1])

    for i in range(Noise_num):
        randY = random.randint(0, src.shape[0]-1)
        randX = random.randint(0, src.shape[1]-1)

        if random.random() >= 0.5:
            Noise_img[randY,randX] = 0
        else:
            Noise_img[randY,randX] = 255

    return Noise_img


img = cv2.imread("lenna.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 以下是自己写的椒盐噪声调用
img_noise = function(img_gray, 0.2)
cv2.imshow("1", img_noise)
# 以下是椒盐噪声的api调用
img_api_noise = util.random_noise(img_gray, mode='salt')
cv2.imshow("2", img_api_noise)
cv2.waitKey()
cv2.destroyAllWindows()