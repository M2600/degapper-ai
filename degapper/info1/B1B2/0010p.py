def area(x, y):
    z = x * y / 2
    return z
a = float(input('底辺 '))
b = float(input('高さ '))
c = area(a, b)
print('面積= ', c)