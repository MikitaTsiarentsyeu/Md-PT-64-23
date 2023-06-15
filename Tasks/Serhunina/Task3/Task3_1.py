#Write a program that takes a string as input from a user and returns the number of vowels in the string.
user_input = input('Enter your string values\n')

vowels = 'aAeEiIoOuUyY'

counter = 0

for letter in user_input:
    if letter in vowels:
       counter +=1
print('The number of vowels is - ', counter)