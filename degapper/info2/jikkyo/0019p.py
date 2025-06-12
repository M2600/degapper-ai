def triangle(x, y, z):
    if x <= 0 or y <= 0 or z <= 0 or x + y <= z or y + z <= x or z + x <= y:
        return 0
    if x == y == z:
        return 3
    if x == y or y == z or z == x:
        return 2
    else:
        return 1