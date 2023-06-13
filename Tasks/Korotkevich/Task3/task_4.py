numbers = input('Please enter the numbers: ')
numbers_new = set(sorted([int(i) for i in numbers]))
print(list(numbers_new)[-2])
