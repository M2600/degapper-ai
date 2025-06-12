import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x1 = [12, 16, 20, 28, 36]
x2 = [1, 1, 0, 2, 1]
y = [700, 900, 1000, 1750, 1800]

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x1, x2, y, marker="o", s=80, c="green")

ax.set_xlim(10, 40)
ax.set_ylim(0, 3)
ax.set_zlim(500, 2000)

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt. show()