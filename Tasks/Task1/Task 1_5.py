import random

def random_number():
    first = input('Enter the LOWER value of the generation range: \n')
    last = input('enter the HIGHER value of the generation range: \n')
    rand_number = random.randint(float(first),float(last))
    print('The random number in range from 'f'{first}'' to 'f'{last}'' = 'f'{rand_number}')
    input('Press Enter to exit...')

try:
    random_number()
except:
    print('Error! The enter must contain the FIRST(lower) and LAST(higher) values in generation range.')
    input('Press Enter to exit...')