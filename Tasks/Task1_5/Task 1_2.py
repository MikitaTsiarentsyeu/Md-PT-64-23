import math
import re

radius_numbers = input('Enter radius of a circle:\n').replace(',','.')

if re.search(r'[a-zA-Zа-яА-я]',radius_numbers):
    print('Enter must contain only numbers, no letters.')
elif len(radius_numbers) == 0:
    print("Input can't be empty.")
elif re.search(r'[!@#$%:,"#?°]',radius_numbers):
    print("Don't use special characters!")
elif re.search(r'[ ]',radius_numbers):
    print("Don't use spaces!")
elif float(radius_numbers) <= 0:
    print('The entered value is too low. The value must be more then 0.')
else:
    area = math.pi*float(radius_numbers)**2
    area = format(area,'.2f')
    print('Area of this circle = 'f'{area}')

