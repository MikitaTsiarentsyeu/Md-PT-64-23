user_input = input('Enter a string:\n')

res = ''
for i in user_input:
    if i.islower():  
        res += i.upper() 
    else:
        res += i.lower()

print(f'Inverted string:\n{res}')