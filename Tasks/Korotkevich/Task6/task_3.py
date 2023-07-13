def summ(listt):
    try:
        xxx = 0
        for i in listt:
            if i % 2 == 0:
                xxx += i
        print(xxx)
    except TypeError:
        print('Invalid input type')

a = [2, 5, 11, 18, 9, 8]
b = [2, 6, 7, 'a']
c = 1
d = 'abc'

summ(a)
print()
summ(b)
print()
summ(c)
print()
summ(d)