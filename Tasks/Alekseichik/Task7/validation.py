import datetime
import logic

def validation_year(year):
    now = datetime.datetime.now().year
    if int(year)<1895 or int(year)> now+5:
        raise ValueError
    else:
        return year
    
def validation_director(arg):
    if not str(arg).replace(' ','').isalpha():
        raise ValueError      
    else:
        return arg

def validation_genre(arg):
    for i in arg:
        if i.isdigit():
            raise ValueError
    return arg

def check_duplicates(title,director,year,genre):
    line = title,director,int(year),genre
    data = logic.to_find_duplicate()
    for i in data:
        i = i[1:]
        if i == line:
            raise ValueError
    return title,director,year,genre

