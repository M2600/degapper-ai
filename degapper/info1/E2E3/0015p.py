if flag.onClick():
    time = 15
    while time != 0:
        wait(1)
        time -= 1
    print("ゲームオーバー")
    StopAll()