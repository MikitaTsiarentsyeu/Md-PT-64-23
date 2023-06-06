def celsius_to_fahrenheit():
    celsius = input('Please, enter °C:\n')
    fahrenheit = float(celsius) * 1.8 + 32
    fahrenheit = format(fahrenheit,'.1f')
    print(f'{celsius}''°C = 'f'{fahrenheit}''°F')
    input('Press Enter to exit...')

try:
    celsius_to_fahrenheit()
except:
    print('Wrong enter! Enter must contain only numbers.')
    input('Press Enter to exit...')