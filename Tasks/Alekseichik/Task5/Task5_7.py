word = 'шалаш'

def is_palindrome(word):
    if len(word) == 1:
        return 'Palindrome'
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return 'No Palindrome'

print(is_palindrome(word))
        