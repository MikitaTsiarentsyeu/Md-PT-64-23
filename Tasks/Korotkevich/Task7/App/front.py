import back

def add_film():
    title = input('Please enter the title: ')
    director = input('Please enter the director: ')
    year = input('Please enter the year: ')
    genre = input('Please enter the genre: ')
    back.add_film(title, director, year, genre)
    return print('Film was added')

def get_all_films():    
    print(back.get_all_film())

def get_film_director_year_genre(choice):
    if choice == '4':
        key = input('Please enter the title of film: ')
        return print(back.search_title(key))
    elif choice == '3':
        key = input('Please enter the director of film: ')
        return print(back.search_director(key))
    elif choice == '2':
        key = input('Please enter the year of film: ')
        return print(back.search_year(key))
    elif choice == '1':
        key = input('Please enter the genre of film: ')
        return print(back.search_genre(key))
        
def start_menu():
    while True:
        answ = input('''
            Choose the menu option:
            3 - Get the film/director/year/genre
            2 - Get all films
            1 - Add the new film
            0 - Exit
                     
            Your choice: ''')
        if answ == '0':
            print('Goodbye')
            break
        elif answ == '1':
            add_film()
        elif answ == '2':
            get_all_films()
        elif answ == '3':
            choice = input('''
                Searche for:
                4 - Title
                3 - Director
                2 - Year
                1 - Genre
                Another value will return you to the main menu
                        
                Your choice: ''')
            get_film_director_year_genre(choice)
        else:
            print('Choose only numbers presented in the list')