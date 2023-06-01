km_h = input(('Please, enter the speed in km/h: ' ))

if '.' in km_h:
    x = km_h[0:km_h.find('.')]
    y = km_h[km_h.find('.')+1:]
    if x.isdigit() and y.isdigit():
        print((float(km_h) * 1000) / 3600, 'm/s')
    else:
        print('You have entered wrong data.')
elif km_h.isdigit():
    print((float(km_h) * 1000) / 3600, 'm/s')
else:
    print('You have entered wrong data.')
