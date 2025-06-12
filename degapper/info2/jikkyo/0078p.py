from scipy.cluster.hierarchy import linkage, dendrogram, set_link_color_palette
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matolotlib

df=pd.read_csv('weather_data.csv', encoding='utf-8')
X = df[['temp', 'rain']].values
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

clusters = linkage(X, method='average', metric='euclidean')
set_link_color_palette(['red', 'green', 'orange', 'cyan', 'magenta', 'yellow'])
dendrogram(clusters, labels=df['pref'].values, color_threshold=2.0)
plt.ylabel('クラスタ間距離')
plt.show()