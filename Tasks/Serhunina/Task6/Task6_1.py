#Write a function that takes two numbers as input and returns their division. Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.

def devision(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
a = int(input())
b = int(input())

print(devision(a,b))