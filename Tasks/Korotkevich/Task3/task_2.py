numbers = input('Please enter the numbers:')
sum_even = 0
for i in numbers:
    if int(i) % 2 == 0:
        sum_even += int(i)
print(sum_even)
