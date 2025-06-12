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