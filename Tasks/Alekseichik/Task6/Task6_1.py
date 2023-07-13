a = float(input('a= '))
b = float(int(input('b= ')))

def division (a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Cannot divide by zero'
    
print(division(a,b))