radius = input('Enter your value for radius:\n')

try:
    float(radius)
except ValueError:
    print('You have entered wrong value')
    exit(1)

radius = float(radius)

const = 3.14
const = float(const)

s = const*(radius*radius)
print(s)