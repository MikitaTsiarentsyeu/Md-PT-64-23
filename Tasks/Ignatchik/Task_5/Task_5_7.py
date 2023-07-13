input_string = 'ASCII stands for American Standard Code for Information Interchange'
input_string_1 = 'iipii'
def palindrome(enter):
    if len(enter) < 1:
        return True
    else:
        if enter[0] == enter[-1]:
            return palindrome(enter[1:-1])
        else:
            return False
        
print(palindrome(input_string))
print(palindrome(input_string_1))