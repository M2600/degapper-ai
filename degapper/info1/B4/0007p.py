def You():
    if button.pressed("1"):
        yourHand = 1
        print("あなたの手はグー")
    else:
        if button.pressed("2"):
            yourHand = 2
            print("あなたの手はチョキ")
        else:
            if button.pressed("3"):
                yourHand = 3
                print("あなたの手はパー")

def Comp():
    compHand = randint(1, 3)
    if compHand == 1:
        print("私の手はグー")
    else:
        if compHand == 2:
            print("私の手はチョキ")
        else:
            if compHand == 3:
                print("私の手はパー")

def Judge():
    judge = yourHand - compHand
    if judge == 0:
        print("あいこ")
        result.append("あいこ")
    else:
        if judge == -1 or judge == 2:
            print("あなたの勝ち")
            result.append("勝ち")
        else:
            print("あなたの負け")
            result.append("負け")

if flag.onClick():
    result = []
    while True:
        print("じゃんけんぽん")
        waitKey()
        You()
        Comp()
        Judge()