numbers = input('Enter numbers:\n').replace(',','').split(' ')

res = []
for number in numbers:
    if int(number)%2 == 0:
        res.append(int(number))

print(f'The sum of even numbers: {sum(res)}')