import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = a.reshape(2, 2)
d = c.reshape(1, -1)
print(a[0], a[3])
print(a[0:2])
print(b[0, 0], b[1, 2])
print(b[0:2, 0:2])
e = np.arange(1, 5, 1)
f = e ** 2
g = e * e
h = np.sqrt(e)