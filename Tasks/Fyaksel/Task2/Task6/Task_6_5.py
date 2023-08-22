# Write a decorator function that caches the return value of a function with a dictionary. If the function is called again with the same arguments, return the cached value instead of computing it again.
# sum(2, 3)   cache = {(2, 3):5}  sum(2, 3)  

def cache(func):
    cache_dict = {}
    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            value = func(*args)
            cache_dict[args] = value
            return value

    return inner

@cache
def sum(*args):
    res=0
    for i in args:
        res+=i
    return res

@cache
def mult(*args):
    res=1
    for i in args:
        res*=i
    return res

print(sum(2,3))
print(sum(2,3))
print(mult(2,3))
print(mult(2,3))