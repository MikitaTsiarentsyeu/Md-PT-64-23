from rounding import rouding
import math
from dots import presence_of_dots
from strings import string_of_numbers

def area_of_a_circle(radius):
    """A function that calculates the area of a circle given a given radius."""
    area = math.pi*radius**2
    return area

if __name__ == "__main__":
    radius = input('Enter the radius of the circle:\n')
    if presence_of_dots(radius):
        radius_string = string_of_numbers(radius)
        result =  area_of_a_circle(float(radius_string))
        x = int(input('Enter the number of decimal places: \n'))
        if x < 1:
            print(f'The area of the circle is {int(result)}')
        else:
            print(f'The area of the circle is {rouding(result, x)}')
    else:
        print('Check your input')