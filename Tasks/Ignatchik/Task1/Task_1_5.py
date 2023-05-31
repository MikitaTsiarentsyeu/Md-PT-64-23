from random import *

def random_number(number1, number2):
    """A function that generates a random number from a given range"""
    res = randint(number1, number2)
    return res
if __name__ == "__main__":
    print('Enter two numbers from the range from which you want to generate a random number')
    num1, num2 = input(), input()
    if num1.isdigit() == True and num2.isdigit() == True:
        result = random_number(int(num1), int(num2))
        print(f'Your number {result}')
    else:
        print('Check your input')  