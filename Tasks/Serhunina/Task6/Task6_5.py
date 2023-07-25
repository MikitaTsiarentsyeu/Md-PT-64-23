#Write a decorator function that caches the return value of a function with a dictionary. If the function is called again with the same arguments, return the cached value instead of computing it again.
#sum(2, 3) #cache = {(2, 3):5} #sum(2, 3)


def cache(function):
    cache_dict = {}
    def wrapper(*args):
       
        if args in cache_dict:
            return cache_dict[args]
        else:
            res = function(*args)
            cache_dict[args] = res
            return res
    return wrapper

@cache
def sum(a, b):
    computing_sum = a+b
    return computing_sum
    

@cache
def mult(a, b):
    return a*b

print(sum(7, 3))
print(sum(7, 3))
print(mult(2, 3))