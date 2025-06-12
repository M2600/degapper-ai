def saiki(n):
    if n != 0:
        return n * saiki(n-1)
    else:
        return 1
i = 5
print(saiki(i))