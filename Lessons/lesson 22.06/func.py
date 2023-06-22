def my_print(a, b, c):
    print(a, b, c)

def my_print(a, b):
    print(a, b)

# my_print(1, 2, 3)

def evalute(arg1, arg2, arg3):
    return arg1*arg2+arg3

print(evalute(arg2=2, arg3=1, arg1=3))
print(evalute(3, arg3=2, arg2=1))
print(1, 2, 3, sep=",", end=".\n")

def sum(*args):
    res = 0
    for i in args:
        res += i
    return res

print(sum(*[1,2,3,4,5]))
print(sum(1,2,3,4,5,6,7,8,9,10))

print(*[1,2,3,4])

def my_print(x, y, *args, a, b):
    print(x)
    print(y)
    print(*args)
    print(a)
    print(b)

my_print(3,4,5,a=1,b=2)


def print_params(**kwargs):
    for i in kwargs:
        print(i)

print_params(test=1,two=2,three=3)

def maximum_flex(x, y, *args, **kwargs):
    print(x, y)
    print(args)
    print(kwargs)

maximum_flex(x=4, y=3)