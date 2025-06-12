import random
i = 1
score = 0
while i <= 3 :
    if random.random() < 0.5 :
        print("ハート")
        score = score + 1
    else :
        print("スペード")
    i = i + 1
print(score)