km_h = input(('Please, enter the speed in km/h: ' ))

if km_h.isdigit():
    print((int(km_h) * 1000) / 3600, 'm/s')
else:
    print('You have entered wrong data.')
