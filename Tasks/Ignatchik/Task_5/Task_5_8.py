input_string = 'ASCII stands for American Standard Code for Information Interchange'

def count(string, symbol):
    if symbol not in string:
        return 0
    elif string[0] == symbol:
        return 1+count(string[1:], symbol)
    else:
        return count(string[1:], symbol)
    
print(count(input_string, 'a'))