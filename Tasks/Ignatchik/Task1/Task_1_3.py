from rounding import rouding
from dots import presence_of_dots
from strings import string_of_numbers

def speed(s):
    """A function that converts kilometers per hour to meters per second."""
    sp = s/3.6
    return sp

if __name__ == "__main__":
    sp = input('Enter speed in kilometers per hour:\n')
    if presence_of_dots(sp):
        string_sp = string_of_numbers(sp)
        result =  speed(float(string_sp))
        x = int(input('Enter the number of decimal places: \n'))
        if x < 1:
            print(f'{int(result)} meters per second')
        else:
            print(f'{rouding(result, x)} meters per second')
    else:
        print('Check your input')        