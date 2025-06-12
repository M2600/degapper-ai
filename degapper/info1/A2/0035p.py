n = int(input("いくつまでの素数を計算しますか"))
activeCell.value = 2
activeCell.offset(1, 0).select
for x in range(3, n, 2):
    s = True
    for i in range(3, sqrt(x), 2):
        if x % i == 0:
            s = False
    if s == True:
        activeCell.value = x
        activeCell.offset(1, 0).select