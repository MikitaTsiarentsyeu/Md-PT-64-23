C = input("Enter your value in Celsius:")
if C.isnumeric():
    C=float(C)
    F = C*1.8+32
    print(f"{C} in Celsius is {F} in Fahrenheit")
else:
    C = input("Please, enter value in numeric format:")
    C=float(C)
    F = C*1.8+32
    print(f"{C} in Celsius is {F} in Fahrenheit")