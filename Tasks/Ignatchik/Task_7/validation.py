numbers_year = 4

def check_year(year):
    year_1 = year.replace(" ","").isdigit()
    if year_1 == True and len(year) == 4:
        res = True
    else:
        res = False# "Not all entered values are numbers"
    return res