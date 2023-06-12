user_input = input('Please, enter a string to remove vowels: \n').lower()

vowels = 'aeyuio'

for i in user_input:
        if i in vowels:
            user_input = user_input.replace(i,'')
print(f'The string without vowels:\n{user_input}')