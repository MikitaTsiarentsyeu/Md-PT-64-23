# Write a recursive function to check whether a given string is a palindrome.
def func(string):
    if len(string)<=1:
        return True
    if string[0] == string[-1]:
        return func(string[1:-1])
    else:
        return False
    
print(func('tenet'))
print(func('шалаш'))
print(func('тутси'))
print(func('sagas'))