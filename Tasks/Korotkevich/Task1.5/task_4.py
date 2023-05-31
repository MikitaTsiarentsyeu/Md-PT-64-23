dollar = input('Please, enter the amount of dollars and ratio via "enter": ' )
ratio = input()

if dollar.isdigit() and '.' in ratio:
    x = ratio[0:ratio.find('.')]
    y = ratio[ratio.find('.')+1:]
    if x.isdigit() and y.isdigit():
        print(float(dollar) * float(ratio), 'BYN')
    else:
        print('You have entered wrong data.')
elif '.' in dollar and '.' in ratio:
    x = ratio[0:ratio.find('.')]
    y = ratio[ratio.find('.')+1:]
    z = dollar[0:dollar.find('.')]
    h = dollar[dollar.find('.')+1:]
    if x.isdigit() and y.isdigit() and h.isdigit() and z.isdigit():
        print(float(dollar) * float(ratio), 'BYN')
    else:
        print('You have entered wrong data.')
elif '.' in dollar and ratio.isdigit():
    z = dollar[0:dollar.find('.')]
    h = dollar[dollar.find('.')+1:]
    if z.isdigit() and h.isdigit():
        print(float(dollar) * float(ratio), 'BYN')
    else:
        print('You have entered wrong data.')
elif dollar.isdigit() and ratio.isdigit():
    print(float(dollar) * float(ratio), 'BYN')
else:
    print('You have entered wrong data.')
