from scipy.cluster.hierarchy import linkage, dendrogram, set_link_color_palette
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matolotlib

df=pd.read_csv('weather_data.csv', encoding='utf-8')
X = df[['temp', 'rain']].values
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)