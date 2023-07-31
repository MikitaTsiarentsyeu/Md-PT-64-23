import datetime

first_film = 1895
current_year = datetime.datetime.now().year

def check_info(year):    
    year = year.replace(" ",'')    
    if not year:
        return[]
    elif first_film <= int(year) <= current_year and year.isdigit():        
        return year
    