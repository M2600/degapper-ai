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
model = LinearRegression()
model.fit(x_train, y_train)

y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)
train_loss = means_squared_error(y_train, y_pred_train)
test_loss = means_squared_error(y_test, y_pred_test)
print('訓練データ誤差:', '{:.2f}'.format(train_loss))
print('テストデータ誤差:', '{:.2f}'.format(test_loss))

x_point = np.arange(np.min(x), np.max(x), 100).reshape(-1, 1)
y_point = model.predict(x_point)
plt.plot(x_point, y_point, color='red')
plt.xlabel('総人口')
plt.ylabel('医師数')
plt.scatter(x_train, y_train, color='blue')
plt.show()