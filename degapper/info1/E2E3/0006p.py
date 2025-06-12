def CreateQ():
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    ans = n1 + n2
    q = f"{n1} + {n2} は？"

if flag.onClick():
    CreateQ()
    x = int(input(q))
    if x == ans:
        print("正解")
    else:
        print("残念")