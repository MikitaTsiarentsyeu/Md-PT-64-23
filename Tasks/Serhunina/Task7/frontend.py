from backend import add_movie, search_director, search_genre, search_title, search_year, movie_list, init_db

def add_new():
    title = input("Enter the title of the movie:\n")
    director = input("Enter the name of the director of the movie:\n")
    year = int(input("Enter the year of the movie:\n"))
    genre = input("Enter the genre of the movie:\n")
    add_movie(title, director, year, genre)
    print("Added successfully!")

def search():
    print('Your searching options are: 1 - title; 2 - director; 3 - year; 4 - genre.')
    user_choice = int(input('Searching option:\n'))
    users_data = input('Enter your value:\n')
    if user_choice==1:
        generator = search_title(users_data)
    elif user_choice==2:
        generator = search_director(users_data)
    elif user_choice==3:
        generator = search_year(users_data)
    elif user_choice==4:
        generator = search_genre(users_data)
    else:
        print('Invalid input!')
        return
    for i in generator:
        print(i)


def start():
    init_db()
    while True:
        print('You can do the following:\n')
        print('1 - Add new movie to the collection;')
        print('2 - List all movies in the collection;')
        print('3 - Search by: title/director/year/genre;')
        print('4 - Quit.')
        your_choice = int(input('Your option:'))
        if your_choice==1:
            add_new()
        elif your_choice==2:
            for movie in movie_list():
                print(movie)
        elif your_choice==3:
            search()
        elif your_choice==4:
            exit(1)
        else:
            print('Invalid input')

if __name__ == '__main__':
    start()

