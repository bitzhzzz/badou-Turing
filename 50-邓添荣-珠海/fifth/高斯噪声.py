import cv2
import numpy as np
from numpy import shape
import random
from skimage import util


def GaussianNoise(src, means, sigma, Proportion):
    Noise_img = src
    Noise_Num = int(Proportion*Noise_img.shape[0]*Noise_img.shape[1])
    for i in range(Noise_Num):
        randY = random.randint(0, src.shape[0]-1)
        randX = random.randint(0, src.shape[1]-1)

        Noise_img[randY, randX] = Noise_img[randY,randX] + random.gauss(means, sigma)

        if Noise_img[randY, randX] < 0:
            Noise_img[randY, randX] = 0
        if Noise_img[randY, randX] > 255:
            Noise_img[randY, randX] = 255

    return Noise_img


img = cv2.imread('lenna.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("1", img_gray)
# 以下是自己写的高斯噪声调用
img_gauss = GaussianNoise(img_gray, 2, 4, 1)
cv2.imshow("2", img_gauss)
# 以下是高斯噪声的api调用
img_api_gauss = util.random_noise(img_gray, mode='gaussian')
cv2.imshow("3", img_api_gauss)
cv2.waitKey()
cv2.destroyAllWindows()