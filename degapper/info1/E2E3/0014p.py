if flag.onClick():
    seikaisu = 0
    for i in range(5):
        n1 = randint(1, 20)
        n2 = randint(1, 20)
        ans = int(input(f"{n1} + {n2}"))
        if n1 + n2 == ans:
            print("正解")
            seikaisu += 1
        else:
            print("不正解")
    print("正解数は", seikaisu, "問です")