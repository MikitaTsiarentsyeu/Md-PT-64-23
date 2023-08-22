import backend

def add_item():
    title = input('Enter the title: ')
    artist_director = input('Enter the artist or director: ')
    year = input('Enter the year: ')
    genre = input('Enter the genre: ')
    backend.add_item(title, artist_director, year, genre)
    print('Item added successfully!')

def list_items():
    print('All items in the collection:')
    for item in backend.get_items():
        print()
        print('Title:', item['title'])
        print('Artist/Director:', item['artist'])
        print('Year:', item['year'])
        print('Genre:', item['genre'])

def search_items():
    search_term = input('Enter the search term: ')
    print('Search results:')
    print()
    print('Search by Title:')
    for item in backend.search_title(search_term):
        print()
        print('Title:', item['title'])
        print('Artist/Director:', item['artist'])
        print('Year:', item['year'])
        print('Genre:', item['genre'])
    print()
    print('Search by Artist/Director:')
    for item in backend.search_artist(search_term):
        print()
        print('Title:', item['title'])
        print('Artist/Director:', item['artist'])
        print('Year:', item['year'])
        print('Genre:', item['genre'])
    print()
    print('Search by Year:')
    for item in backend.search_year(search_term):
        print()
        print('Title:', item['title'])
        print('Artist/Director:', item['artist'])
        print('Year:', item['year'])
        print('Genre:', item['genre'])
    print()
    print('Search by Genre:')
    for item in backend.search_genre(search_term):
        print()
        print('Title:', item['title'])
        print('Artist/Director:', item['artist'])
        print('Year:', item['year'])
        print('Genre:', item['genre'])

def main():
    while True:
        print('1. Add a new item')
        print('2. List all items')
        print('3. Search for an item')
        print('4. Quit')
        choice = input('Enter your choice (1-4): ')
        print()

        if choice == '1':
            add_item()
        elif choice == '2':
            list_items()
        elif choice == '3':
            search_items()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again!\n')

if __name__ == '__main__':
    main()