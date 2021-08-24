import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("lenna.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("1", cv2.Canny(img, 200, 300))
cv2.waitKey()
cv2.destroyAllWindows()
