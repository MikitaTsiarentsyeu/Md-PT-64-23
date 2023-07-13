def revers_list(to_func):
    reversed_list =[]
    for i in to_func:
        i=i[::-1] 
        reversed_list.append(i)
    return reversed_list
    
to_func = ['spisok','dlya','togo','chtoby','otzerkalit']

print(revers_list(to_func))