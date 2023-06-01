from rounding import rouding
from dots import presence_of_dots
from strings import string_of_numbers

def converts_Celsius_to_Fahrenheit(Celsius):
    """A function that converts Celsius to Fahrenheit."""
    Fahrenheit = float(Celsius*1.8 + 32)
    return Fahrenheit

if __name__ == "__main__":
    Cels = input('Enter temperature in degrees Celsius \n')
    if  presence_of_dots:
        Cel_sius = string_of_numbers(Cels)
        result = converts_Celsius_to_Fahrenheit(float(Cel_sius))
        print('Enter the number of decimal places:')
        x = int(input())
        if x < 1:
            print(f'{int(result)} degrees Celcius')
        else:
            print(f'{rouding(result, x)} degrees Celcius')
    else:
        print('Check your input')