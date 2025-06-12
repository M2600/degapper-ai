import matplotlib.pyplot as graph

jinkou = []

x = 81245
r = 81245/80576
for i in range(2018, 2036):
    x = int(x * r)
    jinkou.append(x)
print(x)
graph.plot(range(2018,2036), jinkou)
graph.xticks([2018, 2020, 2025, 2030, 2035])
graph.show()