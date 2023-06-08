def parsefloat(value):
    try:
        return float(value)
    except ValueError:
        print('Invalid value') 
        exit(1)

Celsius = input('Enter your value for Celsius:\n')
Celsius = parsefloat(Celsius)

constant_1 = 1.8
constant_1 = float(constant_1)

constant_2 = int(32)
constant_2 = int(constant_2)

Fahrenheit = (Celsius*constant_1) + constant_2
print('Fahrenheit value equals:', round(float(Fahrenheit),2))