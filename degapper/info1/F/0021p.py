import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('http://www.data.jma.go.jp/endinfo/tenp/list/cev/an_wld.csv', encoding='sjis')
df.head()