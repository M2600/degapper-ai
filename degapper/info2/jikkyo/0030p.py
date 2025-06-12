import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = a.reshape(2, 2)
d = c.reshape(1, -1)