input_string = 'ASCII stands for American Standard Code for Information Interchange'

print(input_string[::-1])

def revers_1(enter): 
    if len(enter) == 1:
        return enter
    return enter[-1] + revers_1(enter[:-1])
result = revers_1(input_string)
print(result)

def revers_2(enter):
    res=''
    for i in range(len(enter)-1,-1,-1):
        res += enter[i]
    return res
result = revers_2(input_string)
print(result)

def revers_3(enter):
    res=''.join(reversed(enter))
    return res
result = revers_3(input_string)
print(result)