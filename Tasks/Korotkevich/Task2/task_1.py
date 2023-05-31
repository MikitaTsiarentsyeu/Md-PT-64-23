temp_C = input('Please, enter the temperature in Celsius: ' )

if temp_C.isdigit():
    temp_F = int(temp_C) * 1.8 + 32
    print(temp_F, 'F')
else:
    print('You have entered wrong data.')
