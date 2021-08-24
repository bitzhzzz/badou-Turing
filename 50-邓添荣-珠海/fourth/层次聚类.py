import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster


X = [[1,2],[3,2],[4,4],[1,2],[1,3]]
# 算出聚类的二维矩阵
Z = linkage(X, 'ward')
# 进行对聚类数目的分解
f = fcluster(Z, 2, 'distance')

# 打印类的排列图，即linkage的返回值以及聚类顺序图
print(Z,'\r\n')
print(f)

# 画出用层次聚类后的树状图
fig = plt.figure(figsize=(5,3))
dendrogram(Z)
plt.show()