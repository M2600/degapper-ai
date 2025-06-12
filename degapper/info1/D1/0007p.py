x = 0
y = 0
vx = 5
vy = 10
t = 0
while t < 300 :
    print("(", x, "," , y, ")")
    x = x + vx
    y = y + vy
    vy = vy - 1
    if y <= 0 :
        break
    t = t + 1
print("(", x, "," , y, ")")