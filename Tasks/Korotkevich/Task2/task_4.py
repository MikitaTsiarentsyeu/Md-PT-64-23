dollar = input('Please, enter the amount of dollars and ratio via "enter": ' )
ratio = input()
if dollar.isdigit() and ratio.isdigit():
    print(int(dollar) * int(ratio), 'BYN')
else:
    print('You have entered wrong data.')
