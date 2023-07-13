#Write a recursive function to find the Nth number in the Fibonacci sequence. 0, 1, 2, 3, 5, 8, 13, 21, ...
def func(fib):
    if fib <= 0:
        return #"Invalid value."
    elif fib == 1:
        return 0
    elif fib == 2:
        return 1
    else:
        return func(fib-1) + func(fib-2)

fib = 2
result = func(fib)
print(result)