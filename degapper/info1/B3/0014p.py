a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
s = 0
for i in range(10):
    a[i] = i + 1
for i in range(1, 10):
    s = s + a[i]
print(s)