Amount = input('USB:\n')

if not Amount.isdecimal():
    print('Wrong value')
    exit(1)
else:
    Amount = int(Amount)
    
    ratio = 2.9152
    ration = float(ratio)

    converting_result = Amount*ratio

    print(round(converting_result,2), 'BYN')