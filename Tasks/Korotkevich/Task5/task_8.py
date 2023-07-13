x = 'aaaaaaaaaazxcvbnaa'

def founder(x, i=0, res=0, f = 'a'):
    if i == len(x):
        return res
    if x[i] == f:
        return founder(x, i+1, res+1)
    else:
        return founder(x, i+1, res)
    
print(founder(x))