# Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols, second for count of the upper case symbols in the initial string.

def argument(line):
    a = 0
    b = 0
    for f in line:
        if f.isupper():
            a+=1
        elif f.islower():
            b+=1
    return a,b
print(argument(input("Enter line  lower case symbols and upper case symbols: ")))