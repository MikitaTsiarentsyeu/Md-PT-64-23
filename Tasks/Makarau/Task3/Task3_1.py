string = input("Enter a string: ")
vowels = [i for i in string if i in "aeiouAEIOU"]
print("Vowels: ", len(vowels))
