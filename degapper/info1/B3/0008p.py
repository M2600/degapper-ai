comp = 0
flag = 1
imin = 6
imax = 15
while flag == 1:
    imid = int((imin + imax) / 2)
    comp = comp + 1
    if cells[imid][1] == cells[2][1]:
        print(cells[imid][2])
        print(cells[imid][3])
        flag = 0
    else:
        if a > target:
            imax = imid - 1
        else:
            imin = imid + 1