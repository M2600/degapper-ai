import random
a = random.randrange (1, 101)
n = int(input("数を入力してください："))
while n != a:
    if n < a:
        print("小さい")
    else:
        print("大きい")
    n = int(input("数を入力してください："))
print("大あたり！")