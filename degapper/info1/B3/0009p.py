comp = 0
for imax in range(8, 5, -1):
    for i in range(6, imax):
        comp = comp + 1
        if cells[i, 1] > cells[i + 1, 1]:
            ino_tmp = cells[i][1]
            iname_tmp = cells[i][2]
            ist_tmp = cells[i][3]
            cells[i][1] = cells[i + 1][1]
            cells[i][2] = cells[i + 1][2]
            cells[i][3] = cells[i + 1][3]
            cells[i + 1][1] = ino_tmp
            cells[i + 1][1] = iname_tmp
            cells[i + 1][1] = ist_tmp
            
