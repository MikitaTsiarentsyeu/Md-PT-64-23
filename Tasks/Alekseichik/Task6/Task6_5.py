import pickle

def cache_this(func):
    with open ('cache.pb','ab'):
        pass
    try:
        with open('cache.pb','rb') as dump_in:
            cache_data = pickle.load(dump_in)
    except EOFError:
        cache_data = {}
    
    def wrapper(*args):
        if f'{func.__name__}{args}' in cache_data.keys():
            return cache_data[f'{func.__name__}{args}']
        else:
            res = func(*args)
            cache_data[f'{func.__name__}{args}'] = res
            with open('cache.pb','wb') as dump_out:
                pickle.dump(cache_data,dump_out)
            return cache_data[f'{func.__name__}{args}']
    return wrapper

@cache_this
def sum(n,m):
    return n+m

@cache_this
def mult(n,m):
    return n*m

@cache_this
def square(n):
    return n**2

print(square(8))