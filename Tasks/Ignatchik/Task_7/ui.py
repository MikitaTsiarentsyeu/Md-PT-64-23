import validation
import logic

def add_new():
    """ask the user for the title, director, year, genre. Then go to logic"""
    title = input("Please enter movie title:\n")
    director = input("Please enter the director's last name:\n")
    year = input("Please enter year of release:\n")
    genre = input("Please enter movie genre:\n")
    year_2 = validation.check_year(year)
    if year_2 == True:
        res = logic.add_new(title,director,year,genre)
        print(res)
    else:
        print("something went wrong while processing the screen year, please try again")  #"Not all entered values are numbers"

def get_all_collection():
    res = logic.get_all_collection()
    print(*res, sep='\n')

def search_data():
    while True:
        search = input("""
                Choose the menu option:
                0. Back to main menu.
                1. Search for a movie by title.
                2. Search for a movie by director.
                3. Search for a movie by year.
                4. Search for a movie by genre.
                """)
        if search == '0':
            break
        elif search == '1':
            title = input("Please enter movie title:\n")
            res = logic.search_title(title)
        elif search == '2':
            director = input("Please enter the director's last name:\n")
            res = logic.search_director(director)
        elif search == '3':
            year = input("Please enter year of release:\n")
            res = logic.search_year(year)
        elif search == '4':
            genre = input("Please enter movie genre:\n")
            res = logic.search_genre(genre)
        for i in res:
            print(i)

def start():
    while True:
        answ = input("""
            Choose the menu option:
            0.exit
            1.get list of all films in the collection.
            2.Add a new movie to the collection.
            3.Search for a movie by title, director, year or genre.
        """).strip()
        if answ == '0':
            break
        elif answ == '1':
            get_all_collection()
        elif answ == '2':
            add_new()
        elif answ == '3':
            search_data()
        else:
            print("choose only numbers presented in the list")
            continue
