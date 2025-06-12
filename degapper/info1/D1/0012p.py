def fib2(n) :
    mem = [0] * (n+1)
    def fib1(n):
        if (n == 1 or n == 2):
            return 1
        elif mem[n] != 0:
            return mem[n]
        else:
            mem[n] = fib1(n-1) + fib1(n-2)
            return mem[n]
    return fib1(n)
print(fib2(10))