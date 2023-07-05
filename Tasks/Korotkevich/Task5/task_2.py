x = ['abc', 'qwe', 'rty']

def reverse(x):
    res = []
    for i in x:
        res.append(i[::-1])        
    return res

print(reverse(x))