def leap(n):
    if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0):
        return True
    else:
        return False