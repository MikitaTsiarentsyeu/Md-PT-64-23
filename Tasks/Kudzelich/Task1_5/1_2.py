import math

try:
    r = float(input("Enter the radius of circle:\n"))
    S = round(math.pi*(r**2), 2)
    print(f"The square of circle is {S}")
except ValueError:
    print("You enter a wrong data")