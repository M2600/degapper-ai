def leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    return n % 4 == 0