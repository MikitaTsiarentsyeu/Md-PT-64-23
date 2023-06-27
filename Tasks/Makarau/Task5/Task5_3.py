def string_filtered (list):
    res= [] 
    for i in list:
        if len(i) > 5:              
            res.append(i)
    return res 
print(string_filtered(input("Enter string list: ").split()))