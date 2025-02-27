import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像的灰度图
img = cv2.imread("lenna.png", 0)
h, w = img.shape[:]
# 把图像从二维转到一维
data = img.reshape((h * w, 1))
data = np.float32(data)
print(data)

# 停止条件
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 设置初始中心点的选择
flags = cv2.KMEANS_RANDOM_CENTERS
# 返回的结果
'''
compactness：紧密度，返回每个点到相应重心的距离的平方和

labels：结果标记，每个成员被标记为分组的序号，如 0,1,2,3,4...等

centers：由聚类的中心组成的数组
'''
compactness, labels, centers = cv2.kmeans(data, 4, None, criteria, 10, flags)
print(labels)
dst = labels.reshape((img.shape[0], img.shape[1]))

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 显示图像
titles = [u'原始图像', u'聚类图像']
images = [img, dst]
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
