import logic
import validation
def add_new():
    title = input("Movie's title:\n")

    while True:
        try:
            director = input("Movie's creator:\n")
            validation.validation_director(director)
        except ValueError:
            print("Director's name must contains only letters")
            continue
        else:
            break
    
    while True:
        try:
            year = input("Realease year:\n")
            validation.validation_year(year)
        except ValueError:
            print("""The entry is not the actual year of the movie's release.
The input must consist of digits.""")
            continue
        else:
            break

    while True:
        try:
            genre = input("Movie's genre:\n")
            validation.validation_genre(genre)
        except ValueError:
            print("The name of genre must be without integers")
            continue
        else:
            break
    try:
        validation.check_duplicates(title,director,year,genre)
        print(logic.add_new(title,director,year,genre))
    except ValueError:
        print('The Movie already exists in your DataBase')       

def get_all():
    data = (logic.get_all())
    for i in data:
        print(i)

def search_title():
    title = input("Movie's title:\n")
    try:
        data = logic.search_title(title)
        for line in data:
            res = (', '.join(str(item) for item in line))
            print(res)
    except TimeoutError:
        print('Nothing found')

def search_director():
    director = input("Movie's director:\n")
    try:
        data = logic.search_director(director)
        for line in data:
            res = (', '.join(str(item) for item in line))
            print(res)
    except TimeoutError:
        print('Nothing found')
        
def search_year():
    year = input("Movie's year:\n")
    try:
        data = logic.search_year(year)
        for line in data:
            res = (', '.join(str(item) for item in line))
            print(res)
    except TimeoutError:
        print('Nothing found')

def search_genre():
    genre = input("Movie's genre:\n")
    try:
        data = logic.search_genre(genre)
        for line in data:
            res = (', '.join(str(item) for item in line))
            print(res)
    except TimeoutError:
        print('Nothing found')

def main_menu():
    while True:
        command = input('''\nPlease, select an item number:\n
    1 - Add new Movie\n
    2 - Get all Movies\n
    3 - Search Movie by title\n
    4 - Search Movie by director\n
    5 - Search Movie by year\n
    6 - Search Movie by genre\n
    7 - Exit\n
    Input just a number:\n''')
        if command == '1':
            add_new()
            
        elif command == '2':
            get_all()
            
        elif command == '3':
            search_title()
            
        elif command == '4':
            search_director()
            
        elif command == '5':
            search_year()
            
        elif command == '6':
            search_genre()
            
        elif command == '7':
            break
        else:
            print('Choose one of the item above. Enter just a number:\n')

    return