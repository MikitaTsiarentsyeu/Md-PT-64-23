import math

a, b, c = input("Enter a:\n"), input("Enter b:\n"), input("Enter c:\n")

if not a.isnumeric() or not b.isnumeric() or not c.isnumeric():
    print("you've entered incorrect data")
    exit()

a, b, c = int(a), int(b), int(c)

D = b*b - 4*a*c

if D < 0:
    print("there are no roots")
elif D == 0:
    x = -b/(2*a)
    print("the single root is ",x)
else:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    print("roots are ", x1, x2)