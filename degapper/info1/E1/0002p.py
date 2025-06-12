import math
def sosu_hantei (n):
    s = int(math.sart(n))
    k = 0
    if n == 1:
        k = 1
    elif n == 2:
        k = 0
    else:
        if n % 2 == 0:
            k = 1
        for i in range(3, s+1, 2):
            if n%i == 0:
                k=1
    if K == 0:
        result = '素数です！'
    else:
        result = '素数ではありません'
    return result