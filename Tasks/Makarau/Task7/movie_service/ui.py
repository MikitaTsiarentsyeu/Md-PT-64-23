import logic
import validation

def start():
    while True:
        answ = input("""
            Choose the menu option
            0.Quit the program         
            1.Add a new movie to the collection
            2.List all movies in the collection
            3.Search for a movie by title, director, year, or genre
        """).strip()
        if answ == '0':
            break
        elif answ == '1':
            add_movie()
        elif answ == '2':
            get_all_movies()
        elif answ == '3':
            search ()
        else:
            print("Choose only numbers presented in the list")
            continue

def ask_for_param(param):
    value = input (f"Enter {param}\n")
    return value

def add_movie():    
    title = ask_for_param("movie title :")
    director = ask_for_param("director :")
    year = ask_for_param("year :") 
    genre = ask_for_param("genre :")
    try:   
        year = validation.check_info(year)
    except ValueError:
        print (f"\n{year} - An error occurred while passing the year value")
        return
    if year:
        res = logic.add_movie(title,director,year,genre)
        print(res)
    else:
        print("Something went wrong while processing info, please do again")

def get_all_movies():
    try:    
        gen = (logic.get_all_movies())
        for i in gen:
            print(i)
    except RuntimeError as e:
        print(e)

def search ():
    while True:    
        parameter_selection = input("""
            Choose a menu option
            0. Back to main menu
            1. Search for movies by title
            2. Search for movies by director
            3. Search movies by year
            4. Search movies by genre
        """).strip()
        if parameter_selection == '0':            
            break
        elif parameter_selection == '1':
            search_title()
        elif parameter_selection == '2':
            search_director()
        elif parameter_selection == '3':
            search_year()
        elif parameter_selection == '4':
            search_genre()
        else:
            print("Choose only numbers presented in the list")
            continue

def search_title():
    title = ask_for_param("movie title :")
    gen = (logic.search_title(title))
    for i in gen:
        print(i)    

def search_director():
    director = ask_for_param("director :")
    gen = (logic.search_director(director))
    for i in gen:
        print(i)

def search_year():
    year = ask_for_param("year :")
    gen = (logic.search_year(year))
    for i in gen:
        print(i)

def search_genre():
    genre = ask_for_param("genre :")
    gen = (logic.search_genre(genre))
    for i in gen:
        print(i)