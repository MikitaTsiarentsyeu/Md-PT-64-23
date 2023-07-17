def separation (a,b):
    try:
        res=a/b
        return print(res)
    except ZeroDivisionError:
        print("Cannot divide by zero")
separation(int(input("Enter dividend ")),int(input("Enter divisor ")))