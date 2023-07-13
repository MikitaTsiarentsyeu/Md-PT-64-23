def cash(func):
    cashe = {}
    def wrapper(*args):
        if args in cashe:
            print(cashe[args])
            # print(cashe)
        else:
            result = func(*args)
            cashe[args] = result
            print(result)
            # print(cashe)
    return wrapper

@cash
def summ(a, b):
    return a**5+b**6

summ(5, 6)
summ(2, 7)
summ(9, 11)
summ(5, 6)