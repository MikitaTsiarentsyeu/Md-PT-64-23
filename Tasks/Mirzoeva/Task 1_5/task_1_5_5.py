import random

a=random.randint(0, 20)
number=int(input("Enter your number:"))
if a != number:
    print("Try again")
else:
    print("You won")