# Task5: random numbers

import random

numbers = []
for i in range(10):
    rnd = random.randint(0, 50)
    numbers.append(rnd)

print(numbers)