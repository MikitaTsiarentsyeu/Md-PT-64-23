# birthdat

birthdate = int(input("Enter birthdate (yy):"))
if birthdate >= 18:
    print("Birthdate ok")
else:
    print("Birthdate no ")



def validate(year):
    if len(year):
        if len(year)==4 and year.isdigit():
            year=int(year)
        if year>=1945 and year<=2023:
            return True
    else:
        return False

birthdate = input("Enter birthdate (yyyy):")
if validate(birthdate):
    print("Birthdate ok")
else:
    print("Birthdate no ")




from datetime import datetime

def validate(date_text):
    try:
        datetime.strptime(date_text,'%d-%m-%Y')
        return True
    except  ValueError:
        return False


birthdate = input("Enter birthdate (dd-mm-yyyy):")
if validate(birthdate):
    print("Birthdate ok")
else:
    print("Birthdate no ")
