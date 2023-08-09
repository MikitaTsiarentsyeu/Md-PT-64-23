# Write a decorator function that caches the return value of a function with a dictionary. If the function is called again with the same arguments, return the cached value instead of computing it again.
import math

def decorator_cache(function1):
    cache = {}
    def inner_function(*args):
        if args in cache:
            return cache[args]
        else:
            result = function1(*args)
            cache[args] = result
            return result
    return inner_function

@decorator_cache
def factorial_sum(x, y):
    return math.factorial(x) + math.factorial(y)

print(factorial_sum(2, 3))
print(factorial_sum(3, 2))
