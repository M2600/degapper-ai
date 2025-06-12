import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

center = [[1.5, 0.5], [0, -0.5], [-2.0, -1.0]]
DSIZE = 30

rn = np. random. rand (DSIZE, 2)
data = [c + (rn / 2) for c in center]
data = np. concatenate(data)

N_clusters = 3

km = KMeans(n_clusters=N_clusters, init='random', max_iter=300, random_state=0)
y_km = km.fit_predict(data)

plt.scatter(data[y_km == 0, 0], data[y_km == 0, 1], c='red', label='cluster 0')
plt.scatter(data[y_km == 1, 0], data[y_km == 1, 1], c='green', label='cluster 1')
plt.scatter(data[y_km == 2, 0], data[y_km == 2, 1], c='orange', label='cluster 2')

plt.grid(True)
plt.legend(loc="upper left")
plt.show()