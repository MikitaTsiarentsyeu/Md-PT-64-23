import math

def circle_area():

    radius_numbers = input('Enter radius of a circle (m, cm or mm):\n')
    radius_numbers = radius_numbers.split()
    area = math.pi*float(radius_numbers[0])**2
    area = format(area,'.2f')
    if len(radius_numbers) == 2:
        print('Area of this circle = 'f'{area}'f'{radius_numbers[1]}''²')
        input('Press Enter to exit...')
    else:
        print('Area of this circle = 'f'{area}')
        input('Press Enter to exit...')

try:
    circle_area()
except:
    print('Input Error! Enter must contain only numbers or numbers with units.')
    input('Press Enter to exit...')