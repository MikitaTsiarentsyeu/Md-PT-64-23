list_input = ['ASCII stands for American Standard Code for Information Interchange',"123456", "1234", "ASCII", "unicode"]

def string_list_1(array):
    return list(filter(lambda x: len(x) > 5, array))
result = string_list_1(list_input)
print(result)

def string_list_2(array):
    new = [i for i in array if len(i) > 5]
    return new
result = string_list_2(list_input)
print(result)