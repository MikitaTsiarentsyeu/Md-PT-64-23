# Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

strings = input('Input strings: ').lower().replace(',','').split(' ')

word_length = []
for word in strings:
    if len(word) > 5:
        word_length.append(word)

print(f'List  strings with more than 5 characters: {word_length}')
