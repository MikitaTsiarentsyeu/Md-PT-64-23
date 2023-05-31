import random

a, b = input('Please, enter two numbers via "enter": ' ), input()

if a.isdigit() and b.isdigit() and int(b) > int(a):
    print(random.randint(int(a), int(b)))
elif a[0] == '-' and a[1:].isdigit() and b.isdigit() and int(b) > int(a):
    print(random.randint(int(a), int(b)))
elif a[0] == '-' and a[1:].isdigit() and b[0] == '-' and b[1:].isdigit() and int(b) > int(a):
    print(random.randint(int(a), int(b)))
else:
    print('You have entered wrong data.')
