user_input = input('Please, enter a string: \n').lower()

vowels = 'aeyuio'
counter = 0
for letter in user_input:
    if letter in vowels:
        counter +=1       

print(f'The number of vowels is {counter}')
