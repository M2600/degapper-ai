if button.pressed("SPACE"):
    costume = loadImage("コスチューム１")
    point = 0
    while True:
        n1 = randint(1, 20)
        n2 = randint(1, 20)
        ans = int(input(f"{n1} + {n2}"))
        if n1 + n2 != ans:
            costume = loadImage("コスチューム２")
            print("不正解")
            costume = loadImage("コスチューム１")
        point = point + ans

if button.pressed("SPACE"):
    time = 30
    while time != 0:
        wait(1)
        time -= 1
    print("ゲームオーバー")
    StopAll()
    