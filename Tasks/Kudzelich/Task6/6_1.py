a, b = int(input("enter a:\n")), int(input("enter b:\n"))

def div(a,b):
    try:
        return f"the result is {round(a/b,2)}"
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(div(a,b))