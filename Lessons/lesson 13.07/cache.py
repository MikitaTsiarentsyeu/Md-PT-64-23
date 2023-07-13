# cache_dict = {} should be here?

def cache(func):
    # cache_dict = {} should be here?
    def wrapper(*args):
        # cache_dict = {} should be here?
        if args in cache_dict:
            return cache_dict[args]
        else:
            res = func(*args)
            cache_dict[args] = res
            return res
    return wrapper

@cache
def sum(a, b):
    return a+b

@cache
def mult(a, b):
    return a*b

sum(2, 3)
sum(2, 3)
print(cache_dict)
print(mult(2, 3))