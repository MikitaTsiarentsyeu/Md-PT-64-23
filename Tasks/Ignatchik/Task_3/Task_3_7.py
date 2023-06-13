import string
input_string = 'ASCII stands for American Standard Code for Information Interchange'

print(input_string.swapcase())


def big_small(enter):
    string_lower = string.ascii_lowercase
    string_upper = string.ascii_uppercase
    dict_upper = dict(zip(string_upper, string_lower))
    dict_lower = dict(zip(string_lower, string_upper))
    output_string = ''
    for i in input_string:
        if i in dict_upper:
            output_string += dict_upper[i]
        elif i in dict_lower:
            output_string += dict_lower[i]
        else:
            output_string += i
    return output_string
result = big_small(input_string)
print(result)