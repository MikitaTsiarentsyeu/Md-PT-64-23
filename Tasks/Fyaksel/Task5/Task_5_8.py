x = 'mmmmaaaaagggggaaaaarrrrraaaaa'

def letter_a(x, i=0, res=0, f = 'a'):
    if i == len(x):
        return res
    if x[i] == f:
        return letter_a(x, i+1, res+1)
    else:
        return letter_a(x, i+1, res)
    
print(letter_a(x))