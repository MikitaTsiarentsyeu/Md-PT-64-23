import json

def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)

def add_item(title, artist, year, genre):
    data = load_data()
    data.append({
        'title': title,
        'artist': artist,
        'year': year,
        'genre': genre
    })
    save_data(data)

def get_items():
    data = load_data()
    for item in data:
        yield item

def search_title(title):
    data = load_data()
    for item in data:
        if item['title'].lower() == title.lower():
            yield item

def search_artist(artist):
    data = load_data()
    for item in data:
        if item['artist'].lower() == artist.lower():
            yield item

def search_year(year):
    data = load_data()
    for item in data:
        if item['year'] == year:
            yield item

def search_genre(genre):
    data = load_data()
    for item in data:
        if item['genre'].lower() == genre.lower():
            yield item