import string
input_string = 'ASCII stands for American Standard Code for Information Interchange'

def big_small(enter):
    string_lower = string.ascii_lowercase
    count_1 = 0
    count_2 = 0
    for i in enter:
        if i in string_lower:
            count_1 += 1
        else:
            count_2 += 1
    return count_1, count_2
result = big_small(input_string)
print(*result, sep = '\n')