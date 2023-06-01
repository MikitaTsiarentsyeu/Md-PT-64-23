dollars = input('Enter amount of USD:\n')
try:
    dollars = float(dollars)
except:
    print('Wrong data entered')
    exit()
if dollars > 0:
    print('Amount of rubbles =', dollars * 2.52)
else:
    print('negative amount')
