import time

def logging(func):
    stack = []
    def wrapper(*args):
        if len(args) == 1:
            stack.append(args[0])
            st = time.time()
            res = func(*args)
            et = time.time()
            res_time = et- st
            if args[0] == int(stack[0]):
                with open('log.txt', 'a') as f:
                    f.write(str(f'func: {func.__name__}, argumet(s): {args[0]}, result: {res}, time: {res_time}\n'))
            return res
        elif len(args) > 1:
            st = time.time()
            res = func(*args)
            et = time.time()
            res_time = et-st
            with open('log.txt', 'a') as f:
                    f.write(str(f'func: {func.__name__}, argumet(s): {args}, result: {res}, time: {res_time}\n'))
            return res
    return wrapper

@logging
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

@logging
def sum(n,m):
    return n+m
@logging
def square(n):
    return n**2

print(square(7))
print(fibo(8))
print(sum(6,5))