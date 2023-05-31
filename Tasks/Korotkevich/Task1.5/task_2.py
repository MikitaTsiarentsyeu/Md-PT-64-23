import math

radius = input('Please, enter the radius of circle(sm): ' )

if '.' in radius:
    x = radius[0:radius.find('.')]
    y = radius[radius.find('.')+1:]
    if x.isdigit() and y.isdigit():
        print(math.pi * float(radius) ** 2, 'sm2')
    else:
        print('You have entered wrong data.')
elif radius.isdigit():
    print(math.pi * float(radius) ** 2, 'sm2')
else:
    print('You have entered wrong data.')
