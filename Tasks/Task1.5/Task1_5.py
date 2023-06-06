import random
import re
first = input('Enter the LOWEST value of the generation range: \n').replace(',','.')
last = input('enter the HIGHEST value of the generation range: \n').replace(',','.')
if re.search(r'[a-zA-Zа-яА-я]',first) or re.search(r'[a-zA-Zа-яА-я]',last):
    print('Enter must contain only numbers, no letters.')
elif len(first) == 0 or len(last) == 0:
    print("Input can't be empty.")
elif re.search(r'[!@#$%:"#?°]',first) or re.search(r'[!@#$%:"#?°]',last):
    print("Don't use special characters!")
elif re.search(r'[ ]',first) or re.search(r'[ ]',last):
    print("Don't use spaces!")
elif float(first) > float(last):
    print("The first value of the generation range can't be HIGHER THEN the last value")
else:
    rand_number = random.uniform(float(first),float(last))
    print('The random number in range from 'f'{first}'' to 'f'{last}'' = 'f'{rand_number}')
    input('Press Enter to exit...')


