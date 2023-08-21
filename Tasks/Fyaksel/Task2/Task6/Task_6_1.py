# Write a function that takes two numbers as input and returns their division. Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
a, b = int(input("Input a=")), int(input("Input b="))
    
print ("division a,b =", (division(a,b)))