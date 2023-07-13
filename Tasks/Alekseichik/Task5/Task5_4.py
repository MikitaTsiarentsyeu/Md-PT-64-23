def case_counter(to_func):
    lower = 0
    upper = 0
    for i in to_func:
        if i == ' ':
            continue 
        if i.islower():
            lower +=1
        else:
            upper +=1
    return(f'lower = {lower}\nupper = {upper}')

to_func = 'Count The Upper Case And Lower Case Symbols In This String'

print(case_counter(to_func))
