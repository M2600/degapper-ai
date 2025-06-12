import matplotlib.pyplot as plt
from sklearn. linear_model import LinearRegression

x = [[12], [16], [20], [28], [36]]
y = [[1700], [900], [1000], [1750], [1800]]

model = LinearRegression()
model.fit(x, y)

price = model.predict([[24]])
print("直径24cmのピザの値段は%s円であると予測できる" % price[0][0])

plt.figure()
plt.scatter(x, y, marker='o', s=80, c='green')
plt.plot(x, model.coef_ * x + model.intercept_)
plt.title('Relation between diameter and price')
plt.xlabel('diameter')
plt.ylabel('price')
plt.axis([0, 50, 0, 2500])
plt.grid(True)
plt.show()