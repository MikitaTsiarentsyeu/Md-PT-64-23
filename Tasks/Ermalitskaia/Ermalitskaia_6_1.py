def division_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Cannot divide by zero'
a, b = float(input()), float(input())
print(division_numbers(a, b))
