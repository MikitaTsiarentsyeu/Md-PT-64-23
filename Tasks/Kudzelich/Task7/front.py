import back

def add_movie():
    title = input("Please enter the movie title:\n")
    director = input("Please enter the movie director:\n")
    year = input("Please enter the movie year:\n")
    genre = input("Please enter the movie genre:\n")
    res = back.add_movie(title, director, year, genre)
    if res:
        print(res)
    else:
        print("Something went wrong while adding the movie, please try again")

def get_all_movies():
    res = back.get_all_movies()
    print(*res, sep="\n")
    # except RuntimeError as er:
    #     print(er)



def start():
    while True:
        user_input = input("""
                        Choose a menu option:
                        1. Add a new movie to the collection
                        2. List all movies in the collection
                        3. Search for a movie by title, director, year or genre
                        0. Quit the program
                        """)
        if user_input == "0":
            print("Good bye!")
            break
        elif user_input == "1":
            add_movie()
        elif user_input == "2":
            get_all_movies()
        elif user_input == "3":
            choice = input("""
                        Choose a menu option:
                        1. Search by title
                        2. Search by director
                        3. Search by year
                        4. Search by genre
                        
                        Any other number will return you to the main menu
                           """)
            if choice =="1":
                value = input("Enter the title:\n")
                res = back.search_title(value)
            elif choice == "2":
                value = input("Enter the director:\n")
                res = back.search_director(value)
            elif choice == "3":
                value = input("Enter the year:\n")
                res = back.search_year(value)
            elif choice == "4":
                value = input("Enter the genre:\n")
                res = back.search_genre(value)
            else:
               continue
            for i in res:
                print(i) 
        else:
            print("Please choose only numbers presented in menu")