n = int(input("いくつまでの素数を計算しますか"))
for x in range(2, n):
    s = True
    for i in range(2, x):
        if x % i == 0:
            s = False
    if s == True:
        activeCell.value = x
        activeCell.offset(1, 0).select