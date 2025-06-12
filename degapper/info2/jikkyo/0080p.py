from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib. pyplot as plt
import japanize_matplotlib
import japanmap as jm

df=pd.read_csv('weather_data.csv', encoding='utf-8')
X = df[['temp', 'rain']].values
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

model = KMeans(n_clusters=4, random_state=0)
model. fit(X)
df['cluster'] = model.predict(X)
colors = {0: 'red', 1: 'green', 2: 'blue', 3: 'cyan', 4: 'magenta', 5: 'yellow', 6: 'black', 7: 'white'}
for i in range(len(df)):
    df.loc[i, 'color'] = colors[df.loc[i, 'cluster']]
    plt.scatter(df['temp'], df['rain'], color=df[ 'color'])

plt.xlabel ('年平均気温(度)')
plt.ylabel ('年降水量(mm)')
plt.grid (True)
plt.show()

pref_colors = {}
for i in range(len(df)):
    pref_colors[df.loc[i, 'pref']] = df.loc[i, 'color']
image = jm.picture(pref_colors)
plt.imshow(image)
plt.axis('off')
plt.show()