'''
关于Canny的调节杠代码(优化)
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt


def Canny_fuction(Low_threshold):
    canny_img = cv2.GaussianBlur(gray, (3, 3), 0)
    canny_img = cv2.Canny(canny_img,
                          Low_threshold,
                          Low_threshold*ratio,
                          apertureSize=kernel_size)

    dst = cv2.bitwise_and(img, img, mask=canny_img)
    cv2.imshow("test", dst)


lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread('lenna.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("test")

#设置调节杠
cv2.createTrackbar("progress bar", "test", lowThreshold,max_lowThreshold,Canny_fuction)

#初始化
Canny_fuction(0)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()