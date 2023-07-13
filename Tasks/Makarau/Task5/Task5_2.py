def list_reverse (list):
    res= []
    for i in list:    
        new_word=i[::-1]    
        res.append(new_word)
    return res
print (list_reverse(input("Enter string list: ").split()))