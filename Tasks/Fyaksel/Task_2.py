# calculates the area of a circle using radius
radius: float = float(input("Enter the radius of the circle in centimeters to calculate the area of the circle: "))
s = (3.14 * (radius*radius)) # the area of the circle in square centimeters
if radius > 0:
    print('Radius the circle %0.2f centimetre, and the area of the circle %0.2f square centimeters.' % (radius, s))
else:
    print("A circle with zero radius is a point. The radius of a circle with a minus value does not exist.")
    exit()