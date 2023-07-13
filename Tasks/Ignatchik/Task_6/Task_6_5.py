import pickle

def cachee(func):
    square = {}
    def wraper(*args):
        for i in args:
            if i in square:
                result = square[i]
            else:
                result = func(*args)
                square[i] = result
        return result
    return wraper


try:
    with open("dic.pickle", 'rb') as f:
        dic = pickle.load(f)
except FileNotFoundError:
    dic = {}

def cache(func):
    def inner(*args):
        if args in dic:
            return dic.get(args)
        else:
            dic[args] = func(*args)
            with open("dic.pickle", 'wb') as f:
                pickle.dump(dic, f)
            return func(*args)
    return inner

@cachee
def squ(a):
    return a**2

@cache
def sq(a):
    return a**2

print(sq(1), squ(1))
print(sq(2), squ(2))
print(sq(3), squ(3))
print(sq(4), squ(4))
print(sq(5), squ(5))
print(sq(2), squ(2))