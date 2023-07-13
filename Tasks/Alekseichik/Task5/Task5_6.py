text = 'String to reverse'

def reverse (text, res=''):
    if len(text) == 0:
        return res
    else:
        return reverse(text[:-1],res+text[-1])
    
print(reverse(text))
        