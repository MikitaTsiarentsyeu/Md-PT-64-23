#reverse_string

string = "ALEKS"

def reverse(string, res='', i = 1):
    if i > len(string):
        return res
    res += string[-i]
    return reverse(string, res, i+1)

print(reverse(string))