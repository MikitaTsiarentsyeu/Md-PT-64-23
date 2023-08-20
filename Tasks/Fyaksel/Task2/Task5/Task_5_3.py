# Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def string(list):
    res= [] 
    for a in list:
        if len(a) > 5:              
            res.append(a)
    return res 
print(string(input("Enter string list: ").split()))