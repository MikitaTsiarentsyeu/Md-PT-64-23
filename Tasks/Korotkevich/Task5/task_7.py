x = 'спел лепс'

def palindrome(x):
    if len(x) <= 1:
        return 'Palindrome'
    else:
        if x[0] == x[-1]:
            return palindrome(x[1:-1])
        else:
            return 'Not palindrome'
        
print(palindrome(x))