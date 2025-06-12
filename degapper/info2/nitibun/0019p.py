def get_list():
    d_list = []
    for i in range(N) :
        d = ((target[0] - data[i][0]) ** 2 + (target[1] - data[i][1]) ** 2) ** (1 / 2)
        d_list.append([d, data[i][2]])
    return sorted(d_list)