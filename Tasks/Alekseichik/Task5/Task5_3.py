def five_filter(to_func):
    more_then_5 =[]
    for i in to_func:
        if len(i)>5:
            more_then_5.append(i)
    return more_then_5
    
to_func = ['spisok','dlya','togo','chtoby','udalit','stroki','menshe','5']

print(five_filter(to_func))