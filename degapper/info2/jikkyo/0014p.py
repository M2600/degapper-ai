def solution1(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return 0
    else:
        return (-b + d ** 0.5) / (2 * a)