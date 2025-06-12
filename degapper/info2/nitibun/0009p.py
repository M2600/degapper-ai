import matplotlib.pyplot as plt

x = [[12], [16], [20], [28], [36]]
у = [[700], [900], [1000], [1750], [1800]]

plt.figure()
plt.scatter(x, y, marker='o', s=80, c='green')
plt.title('Relation between diameter and price')
plt.xlabel('diameter')
plt.ylabel('price')
plt.axis([0, 50, 0, 2500])
plt.grid(True)
plt.show()