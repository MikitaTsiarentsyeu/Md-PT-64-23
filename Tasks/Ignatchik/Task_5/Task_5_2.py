list_input = ['ASCII stands for American Standard Code for Information Interchange',"123456", "1234", "ASCII", "unicode"]

def revers(list_string):
    result = [i[::-1] for i in list_string]
    return result

print(revers(list_input))