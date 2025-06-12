from scipy.cluster.hierarchy import linkage, dendrogram, set_link_color_palette
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matolotlib

df=pd.read_csv('weather_data.csv', encoding='utf-8')
plt.scatter(df['temp'], df['rain'])
plt.xlabel ('年平均気温(度)')
plt.ylabel ('年降水量(mm)')
plt.grid (True)
plt.show()