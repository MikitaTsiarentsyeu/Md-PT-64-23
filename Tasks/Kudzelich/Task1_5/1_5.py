import random

try:
    start_num = int(input("Enter the start number of the range:\n"))
    end_num = int(input("Enter the end number of the range:\n"))
    print("The random number in your range is", random.randint(start_num, end_num), end = ".")
except ValueError:
    print("You enter a wrong data")