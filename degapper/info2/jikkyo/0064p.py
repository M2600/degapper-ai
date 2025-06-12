import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from sklearn.linear_model import LinearRegression

df = pd.read_csv('SSDSE-2020A.csv', skiprows=[0, 1], encoding='utf-8')
df = df[['市区町村', '総人口', '医師数']]