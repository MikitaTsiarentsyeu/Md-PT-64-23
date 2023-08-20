# Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

def reverse (list):
    res= []
    for i in list:    
        new_word=i[::-1]    
        res.append(new_word)
    return res
print (reverse(input("Enter string list: ").split()))
