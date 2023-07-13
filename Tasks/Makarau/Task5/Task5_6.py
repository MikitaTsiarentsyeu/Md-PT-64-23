def my_reverse (string):    
    if len(string) == 0:
        return string
    else:        
        return my_reverse(string[1:]) + string[0]
print(my_reverse(input("Enter string: ")))