import random

my_number = random.randint(1, 10)

your_number = input("Guess a number from 1 to 10:\n")

print(type(your_number))
if your_number.isdigit():
    your_number = int(your_number)
else:
    print("Your eneter a wrong data")
    exit()
    

if 1 <= your_number <= 10:
    if your_number == my_number:
        print("Lucky guess!")
    else:
        print("Looooser!")
else:
    print("Your eneter a wrong data")
