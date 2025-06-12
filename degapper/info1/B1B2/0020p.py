def sale(x):
    global s
    if s == 0 and x == 50:
        print('累計 50円'); s = 50
    elif s == 50 and x == 50 or s == 0 and x == 100:
        print('累計 100円'); s = 100
    elif s == 50 and x == 100 or s == 100 and x == 50:
        print('商品'); s = 0
    elif s == 100 and x == 100:
        print('商品と釣錢50円'); s = 0
S = 0
while True:
    i = int(input('金額の入力（50 or 100 終了は0) '))
    if i == 50 or 4 == 100:
        sale(i)
    elif i == 0:
        break