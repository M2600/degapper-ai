import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('weather_data.csv', encoding='utf-8')

plt.xlabel('降水量')
plt.hist(df['rain'])
plt.show()