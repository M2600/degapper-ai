from sklearn. linear_model import LinearRegression

x1 = [12, 16, 20, 28, 36]
x2 = [1, 1, 0, 2, 1]
y = [700, 900, 1000, 1750, 1800]

x = [[i, j] for i, j in zip(x1, x2)]
y = [[i] for i in y]

model = LinearRegression()
model.fit(x,y)