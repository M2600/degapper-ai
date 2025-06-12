import numpy as np
import matplotlib.pyplot as plt

center = [[1.5, 0.5], [0, -0.5], [-2.0, -1.0]]
DSIZE = 30

rn = np.random.rand(DSIZE, 2)
data = [c + (rn / 2) for c in center]
data = np.concatenate(data)

plt.scatter(data[:, 0], data[:, 1])
plt.grid(True)
plt.show()