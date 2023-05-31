import math

radius = input('Please, enter the radius of circle(sm): ' )

if radius.isdigit():
    print(math.pi * int(radius) ** 2, 'sm2')
else:
    print('You have entered wrong data.')
