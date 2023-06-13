input_string = 'ASCII stands for American Standard Code for Information Interchange'

def word_counter(enter):
    enter = enter.lower().strip()
    new_line = ''
    for i in enter:
        if 97 <= ord(i) <= 122 or ord(i) == 32:
            new_line += i
    word_list = new_line.split(' ')
    res = {index: elem for index, elem in enumerate(word_list)}
    return res

result = word_counter(input_string)
print(result)