try:
    C = input("Enter your value in Celsius:\n")
    C=float(C)
    F = round(C*1.8+32, 2)
    print(f"{C} in Celsius is {F} in Fahrenheit")
except ValueError:
    print("You enter a wrong data")