#Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols, second for count of the upper case symbols in the initial string.

def func(string):
    lower_c = 0
    upper_c = 0
    for s in string:
        if s.islower():
            lower_c +=1
        elif s.isupper():
            upper_c +=1
            
    return lower_c, upper_c

string = ('MinI hello Y arE u So saD?')
res = func(string)
print(res)



    
    