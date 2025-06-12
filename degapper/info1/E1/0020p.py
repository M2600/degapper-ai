import random
data = []
for i in range(10):
    data.append(random.randint(1, 99))
atai = 70
for i in range(10):
    if data[i] == atai:
        print("見つかりました")
        break
for i in range(0, 9, 1):
    for j in range(i + 1, 10, 1):
        if data[i] > data[j]:
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp
print(data)