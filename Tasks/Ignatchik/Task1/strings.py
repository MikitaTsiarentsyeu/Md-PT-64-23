def string_of_numbers(string_1):
    """A function that forms a string from numbers and a dot"""
    string_2 = '0123456789.'
    string_3 = ''
    for i in string_1:
        for j in string_2:
            if j == i:
                string_3 += i
    return string_3