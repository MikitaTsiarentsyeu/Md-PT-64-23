numbers = input('Please enter the numbers with space: ').split(' ')
new_numbers = []
for i in numbers:
    if int(i) == 2 or int(i) == 3:
        new_numbers.append(int(i))
    if int(i) % 2 == 0 or int(i) % 3 == 0 or int(i) % 5 == 0 or int(i) % 7 == 0:
        continue
    else:
        new_numbers.append(int(i))
print(max(new_numbers))
