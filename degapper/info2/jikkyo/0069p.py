import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.processing import PolynomialFeatures
from sklearn.model_selection import train_test_split

df = pd.read_csv('SSDSE-2020A.csv', skiprows=[0, 1], encoding='utf-8')
df = df[['市区町村', '総人口', '医師数']]
df.loc[df['総人口'] == 0, '総人口'] = None
df.dropna()

for c in ['総人口', '医師数']:
    q1 = df[c].quantile(0.25)
    q3 = df[c].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - iqr * 1.5
    upper = q3 - iqr * 1.5
    df.loc[(df[c] < lower) | (df[c] > upper), c] = None
df = df.dropna()

x = df[['総人口']].values
y = df['医師数'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

n = 10
poly = PolynomialFeatures(degree=n, include_bias=False)
poly_x_train = poly.fit_transform(x_train)
poly_x_test = poly.fit_transform(x_test)
model = LinearRegression(normalize=True)
model.fit(poly_x_train, y_train)
y_pred_train = model.predict(poly_x_train)
y_pred_test = model.predict(poly_x_test)