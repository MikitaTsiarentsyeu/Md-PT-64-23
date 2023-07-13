input_string = 'ASCII stands for American Standard Code for Information Interchange'

def revers_1(enter): 
    if len(enter) == 1:
        return enter
    return enter[-1] + revers_1(enter[:-1])
result = revers_1(input_string)
print(result)