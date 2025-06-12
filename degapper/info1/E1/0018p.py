import random
num = 1000000
inner = 0
for i in range(num):
    x = random.random ()
    y = random.random ()
    if x * x + y * y < 1:
        inner = inner + 1
print (inner * 4 / num)