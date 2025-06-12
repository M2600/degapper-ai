Randomize()
z = 0
for n in range(1, 11):
    x = random()
    y = random()
    r = x ** 2 + y ** 2
    r = sqrt(r)
    if r <= 1:
        x = x + 1
p = z / (n - 1) + 4
print(p)