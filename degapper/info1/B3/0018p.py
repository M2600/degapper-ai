n = 100
count = 0
for i in range(1, n + 1):
    x = random()
    y = random()
    if x * x + y + y <= 1:
        count = count + 1
pi = count / n * 4
print(n)
print(count)
print(pi)