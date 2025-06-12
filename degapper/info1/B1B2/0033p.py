def kaijo(n):
    j =1
    for i in range(n, 0, -1):
        j = j * i
    return j
x = 5
print(kaijo(x))