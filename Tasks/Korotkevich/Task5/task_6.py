x = 'qwerty'

def reverse(x, res='', i = 1):
    if i > len(x):
        return res
    res += x[-i]
    return reverse(x, res, i+1)

print(reverse(x))