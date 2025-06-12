if flag.onClick():
    coin10 = int(input("10円硬貨は何枚？"))
    coin50 = int(input("50円硬貨は何枚？"))
    coin100 = int(input("100円硬貨は何枚？"))
    goukeiMaisu = coin10 + coin50 + coin100
    print("合計枚数は", goukeiMaisu)
    goukeiKingaku = coin10 * 10 + coin50 * 50 + coin100 * 100
    print("合計金額は", goukeiKingaku)