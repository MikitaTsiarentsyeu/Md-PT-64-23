#Generating a random number from a given range
import random
a = float(input("Enter enter the number of the beginning of the range a="))
b = float(input("Enter enter the number of the end of the range b="))
r = float(random.uniform(a,b))
print('Random number = ',r, sep='', end='\n')