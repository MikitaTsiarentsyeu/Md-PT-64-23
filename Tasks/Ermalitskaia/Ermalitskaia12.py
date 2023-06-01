from math import pi
radius = input('Enter radius of a circle:\n')
try:
    radius = float(radius)
except:
    print('radius should be a number')
    exit()
if radius > 0:
    print('Area of the circle =', pi * radius ** 2)
else:
    print('Wrong data')