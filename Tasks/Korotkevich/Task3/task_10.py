numbers = input('Please enter the numbers with space: ').split(' ')
new_numbers = []
for i in numbers:
    counter = 0
    for j in range(1, int(i)):
        if int(i) % int(j) == 0:
            counter += 1
    if counter == 1:
        new_numbers.append(int(i))
    counter = 0
print(max(new_numbers))
