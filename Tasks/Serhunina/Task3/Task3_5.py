#Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
user_input = input('Enter your string values\n')
user_input = user_input.split()

list_of_str = []

for charac in user_input:
    if len(charac)>5:
        list_of_str.append(charac)
print(f'Your strings which length are greater than 5 characters',list_of_str)