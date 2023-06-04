import re

celsius = input('Please, enter °C:\n').replace(',','.')

if re.search(r'[a-zA-Zа-яА-я]',celsius):
    print('Enter must contain only numbers, no letters.')
elif len(celsius) == 0:
    print("Input can't be empty.")
elif re.search(r'[!@#$%:,)(_}{"#?°=]',celsius):
    print("Don't use special characters!")
elif re.search(r'[ ]',celsius):
    print("Don't use spaces!")
elif float(celsius) < -273.15:
    print('The entered °C value is too low. The value must be more then -275.15.')
else:
    fahrenheit = float(celsius) * 1.8 + 32
    format(fahrenheit, '.0f')
    print(f'{celsius}''°C = 'f'{fahrenheit}''°F')