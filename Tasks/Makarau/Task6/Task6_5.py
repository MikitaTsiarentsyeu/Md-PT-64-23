def cache (func):
    cache_dict = {}
    def wrapper(*args):        
        if args not in cache_dict:
            res=func (*args)
            cache_dict [args] = res
            return res
        return cache_dict [args]            
    return wrapper

@cache
def my_sum (a, b):
    return a+b

@cache
def my_mult (a, b):
    return a*b

print(my_sum (2, 3))
print(my_sum (2, 3))

print(my_mult (2, 3))
print(my_mult (2, 3))