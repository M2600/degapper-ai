import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([-1, 0, 1])
y1 = np.array([0, 0.5, 1])
plt.scatter(x1, y1)
plt.show()
plt.plot(x1, y1)
plt.show()
x2 = np.arange(-1, 1.1, 0.1)
y2 = x2 ** 2
plt.plot(x2, y2)
plt.show()