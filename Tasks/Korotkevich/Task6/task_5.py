def cash(func):
    cashe = {}
    def wrapper(*args):
        if args in cashe:
            # print(cashe)
            return cashe[args]
        else:
            result = func(*args)
            cashe[args] = result
            # print(cashe)
            return result
    return wrapper

@cash
def summ(a, b):
    return a**5+b**6

@cash
def summm(a, b):
    return a+b

print(summ(5, 6))
print(summ(2, 7))
print(summ(9, 11))
print(summ(5, 6))
print()
print(summm(5, 6))