if flag.onClick():
    yakusuCount = 0
    warukazu = 1
    suti = int(input("数値を入力してください"))
    while suti > warukazu:
        if suti % warukazu == 0:
            yakusuCount += 1
        warukazu += 1
    print("約数の個数は", yakusuCount)