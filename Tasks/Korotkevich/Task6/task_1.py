# while True:
#     a, b = int(input('Enter the numbers ')), int(input())
#     try:
#         a / b
#         print(a / b)
#         break
#     except ZeroDivisionError:
#         print('Cannot divide by zero')
#         print('Try again')
#         continue        

def division(a, b):
    try:
        a / b
        print(a / b)
    except ZeroDivisionError:
        print('Cannot divide by zero')

division(5, 0)
print()
division(12, 2)