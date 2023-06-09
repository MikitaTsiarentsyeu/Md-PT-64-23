numbers = input('Please enter the numbers with space: ').split(' ')
new_numbers = [int(x) for x in numbers]
print(sum(new_numbers) / len(numbers))
