if flag.onClick():
    n1 = randint(1, 20)
    n2 = randint(1, 20)
    ans = int(input(f"{n1} + {n2}"))
    print(ans)
    if n1 + n2 == ans:
        print("正解")
    else:
        print("不正解")