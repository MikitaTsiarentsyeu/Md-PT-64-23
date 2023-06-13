input_string = 'ASCII stands for American Standard Code for Information Interchange'

def deletion_of_vowels(enter):
    vowel = "aeiouyAEIOUY"
    res = ''
    for item in enter:
        if item not in vowel:
            res += item
    return res

result = deletion_of_vowels(input_string)
print(result)