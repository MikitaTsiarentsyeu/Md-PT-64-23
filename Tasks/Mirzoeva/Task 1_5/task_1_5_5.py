import random

a=random.randint(0, 20)
print(a)
number=int(input("Enter your number:"))
if a != number:
    print("Try again")
else:
    print("You won")