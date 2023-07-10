def cache(func):
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

@cache
def sq(a):
    return a**2

print(sq(1))
print(sq(2))
print(sq(3))
print(sq(4))
print(sq(5))
print(sq(2))
