# Write a program that takes a string as input and returns the string with all vowels removed.

string = input("Input string values:  ")
vowels = 'AaEeIiOoUuYy'

for write in string:
    if write in vowels:
        string = string.replace(write, '')
print('The string with all vowels removed:  ', string)


