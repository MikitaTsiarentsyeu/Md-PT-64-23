# Fibonacci sequence: 0,1,1,2,3,5,8,13,21...

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(int(input("enter the number:\n"))))