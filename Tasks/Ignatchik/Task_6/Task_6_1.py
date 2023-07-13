def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"

x, y = int(input()), int(input())
print(division(x,y))