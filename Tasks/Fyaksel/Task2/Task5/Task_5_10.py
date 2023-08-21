n = 10

def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(n))