import matplotlib.pyplot as plt

data = [[8, 4, 'B'], [2, 6, 'B'], [5, 7, 'A'], [7, 1, 'B'], [7, 5, 'A'],
        [10, 6, 'A'] [3, 2, 'B'], [8, 8, 'A'], [1, 9, 'B'], [4, 4, 'B']]

N = len(data)

for i in range(N):
    if data[i][2] == 'A':
        marker_g = '$A$'
        color_g = 'green'
    else:
        marker_g = '$B$'
        color_g = 'blue'
    plt.scatter(data[i][0], data[i][1], marker=marker_g, c=color_g, s=80)

plt.xticks(range(12))
plt.yticks(range(12))
plt.grid(True)
plt.show()