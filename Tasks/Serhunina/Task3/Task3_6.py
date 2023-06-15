#Write a program that takes a string as input and returns the string with all vowels removed.
user_input = input("Enter your string values\n")

vowels_to_be_rmv = 'aAeEiIoOuUyY'

for letter in user_input:
    if letter in vowels_to_be_rmv:
        user_input = user_input.replace(letter, '')
print('Your string values without any vowels are', user_input)