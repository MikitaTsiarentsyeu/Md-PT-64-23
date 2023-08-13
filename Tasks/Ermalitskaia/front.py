import back

def add_article():
    title = input("Please enter the article title:\n")
    author = input("Please enter the article author:\n")
    year = input("Please enter the article year:\n")
    issue = input("Please enter the article issue:\n")
    res = back.add_article(title, author, year, issue)
    if res:
        print(res)
    else:
        print("Something went wrong while adding the article, please try again")
        
def get_all_articles():
    res = back.get_all_articles()
    print(*res, sep="\n")

def start():
    while True:
        user_input = input("""
                        Choose a menu option:
                        1. Add a new article to the library
                        2. List all articles in the library
                        3. Search for a article by title, author, year or issue
                        0. Quit the program
                        """)
        if user_input == "0":
            print("No articles were found")
            break
        elif user_input == "1":
            add_article()
        elif user_input == "2":
            get_all_articles()
        elif user_input == "3":
            choice = input("""
                        Choose a menu option:
                        1. Search by title
                        2. Search by author
                        3. Search by year
                        4. Search by issue

                        Any other number will return you to the main menu
                           """)
            if choice == "1":
                value = input("Enter the title:\n")
                res = back.search_title(value)
            elif choice == "2":
                value = input("Enter the author:\n")
                res = back.search_author(value)
            elif choice == "3":
                value = input("Enter the year:\n")
                res = back.search_year(value)
            elif choice == "4":
                value = input("Enter the issue:\n")
                res = back.search_issue(value)
            else:
                continue
            for i in res:
                print(i)
        else:
            print("Please choose only numbers from the menu")