temp_C = input('Please, enter the temperature in Celsius: ' )

if '.' in temp_C:
    if not temp_C[0] == '-':
        x = temp_C[0:temp_C.find('.')]
        y = temp_C[temp_C.find('.')+1:]
        if x.isdigit() and y.isdigit():
            temp_F = float(temp_C) * 1.8 + 32
            print(temp_F, 'F')
        else:
            print('You have entered wrong data.')
    else:
        x = temp_C[1:temp_C.find('.')]
        y = temp_C[temp_C.find('.')+1:]
        if x.isdigit() and y.isdigit():
            temp_F = float(temp_C) * 1.8 + 32
            print(temp_F, 'F')
        else:
            print('You have entered wrong data.')
elif temp_C.isdigit():
    temp_F = int(temp_C) * 1.8 + 32
    print(temp_F, 'F')
elif temp_C[0] == '-' and temp_C[1:].isdigit():
    temp_F = int(temp_C) * 1.8 + 32
    print(temp_F, 'F')
else:
    print('You have entered wrong data.')
