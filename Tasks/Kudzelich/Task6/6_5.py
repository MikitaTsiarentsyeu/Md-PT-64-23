def decor(func):
    cache_dict = {}
    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            value = func(*args)
            cache_dict[args] = value
            return value

    return inner

@decor
def sum(*args):
    res=0
    for i in args:
        res+=i
    return res

@decor
def mult(*args):
    res=1
    for i in args:
        res*=i
    return res

print(sum(2,3))
print(sum(2,3))
print(mult(2,3))
print(mult(2,3))