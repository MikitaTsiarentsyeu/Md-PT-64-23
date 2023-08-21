# Write a program that takes a string as input and returns a dictionary with the count of each word in the string

string = input('Input words:   ').lower().replace(',','').split(' ')
counter = {}

for words in string:
    if words not in counter:
        counter[words] = 0
    counter[words] += 1
    
for word,quantity in counter.items():
    print(f'{word}: {quantity}')