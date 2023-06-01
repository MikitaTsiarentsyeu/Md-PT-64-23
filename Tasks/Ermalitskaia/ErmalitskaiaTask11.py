celcius = input('Enter temperature in Celcius:\n')
try:
    celcius = float(celcius)
except:
    print('Wrong value - should be a number')
    exit()
if celcius > -273:
    print(celcius, 'Celcius =', celcius * 1.8 + 32, 'Fahrenheit')
else:
    print('Wrong data')

