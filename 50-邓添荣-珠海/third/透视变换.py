import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("photo1.jpg")
result = img.copy()
#通过plt来确定纸四角的位置
#plt.imshow(img)
#plt.show()

src = np.float32([[202, 149], [516, 281], [12, 595], [337, 728]])
dst = np.float32([[0, 0], [337, 0], [0, 488], [337, 488]])

# 生成透视变换矩阵；进行透视变换
m = cv2.getPerspectiveTransform(src, dst)
print(m)
#生成透视变换后的图像
img_warp = cv2.warpPerspective(result, m, (337, 488))
cv2.imshow("1", result)
cv2.imshow("2", img_warp)
cv2.waitKey()
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()