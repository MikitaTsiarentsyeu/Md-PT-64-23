import random
#запрос
x = float(input("Enter the start value of the range\n"))
y = float(input("Enter the end value of the range\n"))
#вычисление
z = random.randint(x,y)
#вывод результата
print("Your random number",z)