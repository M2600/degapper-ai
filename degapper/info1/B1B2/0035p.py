import random
import matplotlib.pyplot as plt
n = 5000
count = 0
for i in range(n):
    ux = random.random()
    uy = random.random()
    if ux * ux + uy * uy <= 1.0:
        count = count + 1
        plt.scatter(ux, uy, color="red", s=5)
    else:
        plt.scatter(ux, uy, color="blue", s=5)
print("円周率 =", count / n * 4)
plt.title("Monte Carlo method")
plt.xlabel("random numbers(x)")
plt.ylabel("random numbers(y)")
plt.show()