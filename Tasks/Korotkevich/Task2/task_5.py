import random

a, b = input('Please, enter two numbers via "enter": ' ), input()

if a.isdigit() and b.isdigit() and int(b) > int(a):
    print(random.randint(int(a), int(b)))
else:
    print('You have entered wrong data.')
