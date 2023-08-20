# Write a program that takes a string as input from a user and returns the number of vowels in the string.

# data = str(input("Please type a sentence: "))
# vowels = "aeiou"
# for v in vowels:
#     print(v, data.lower().count(v))
    
vowel = ['A','a','E','e','I','i','O','o','U','u']

Sentence = input("Enter a phrase: ") 
count = 0
for letter in Sentence:
    if letter in vowel:
        count += 1
print ('vowel =', count )