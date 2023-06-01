import random
a = input('Enter first number:\n')
b = input('Enter second number:\n')
try:
    a = float(a)
except:
    print('wrong value of a - should be a number')
    exit()
try:
    b = float(b)
except:
    print('wrong value of b - should be a number')
    exit()
print(random.randint(a,b))
