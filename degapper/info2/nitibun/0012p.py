from sklearn. linear_model import LinearRegression

x = [[12], [16], [20], [28], [36]]
у = [[700], [900], [1000], [1750], [1800]]

model = LinearRegression()
model.fit(x, y)
score = model.score(x, y)
print("r-squared:", score)