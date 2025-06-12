import matplotlib.pyplot as plt

def get_list():
    d_list = []
    for i in range(N) :
        d = ((target[0] - data[i][0]) ** 2 + (target[1] - data[i][1]) ** 2) ** (1 / 2)
        d_list.append([d, data[i][2]])
    return sorted(d_list)

def knn(k, d_list):
    cnt_A = cnt_B = 0
    for i in range(k):
        if d_list[i][1] == 'A':
            cnt_A += 1
        else:
            cnt_B += 1
    if cnt_A > cnt_B:
        result = 'A'
    elif cnt_A < cnt_B:
        result = 'B'
    else:
        result = '-'
    return (k, result)

data = [[8, 4, 'B'], [2, 6, 'B'], [5, 7, 'A'], [7, 1, 'B'], [7, 5, 'A'],
        [10, 6, 'A'], [3, 2, 'B'], [8, 8, 'A'], [1, 9, 'B'], [4, 4, 'B']]

N = len(data)

target = [5, 5]

sorted_list = get_list()
group = knn(3, sorted_list)
print('k: ', group[0], 'judge: ', group[1])
