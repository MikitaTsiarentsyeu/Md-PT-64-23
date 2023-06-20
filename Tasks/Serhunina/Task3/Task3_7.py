#Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.
user_input = input('Enter your string value\n')
output = ''
for letter in user_input:
    if letter.isupper():
        output += letter.lower()
    else:
        output += letter.upper()
print('The output is:',output)
