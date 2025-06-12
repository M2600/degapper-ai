flag = 1
i = 6
comp = 0
while flag == 1:
    if cells[i][1] == cells[2][1]:
        print(cells[i][2])
        print(cells[i][3])
        flag = 0
    else:
        i = i + 1