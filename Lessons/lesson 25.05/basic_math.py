import decimal
import fractions
import math
import random

x = 5
print(type(x))

print(type(12//x))

x = int(-2.8)
print(x, type(x))

# print(type(int('5.0'))) error

print(type(5.5))
print(1.1+1.1+1.1)

print(type(10/5))
print(type(10.5+5))

print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))

print(round(2.555555555, 3))

x = decimal.Decimal(1.1)
print(x+x+x)

x = decimal.Decimal('1.1')
print(x+x+x)

print(x+1)

x = fractions.Fraction('1.1')
print(x*x)

print(type(math.inf))
print(7547658587576546547857 > -math.inf)

print(2*math.inf)

print(math.nan == math.nan)

print(math.pow(2, 3))
print(2**3)

print(math.sqrt(144))
print(144**0.5)

print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))