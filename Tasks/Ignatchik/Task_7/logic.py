import movie_data

def add_new(title,director,year,genre):
    film = {}
    film = {"title_rus": title, "director": director, "year": year, "genre": genre}
    if film not in movie_data.data:
        movie_data.data.append(film)
        res = "data has been added"
    else:
        res = "this entry already exists"
    return res

def get_all_collection():
    count = 1
    res = []
    for i in movie_data.data:
        res.append(f'{count} - {i["title_rus"]}')
        count += 1
    return  res


def search_title(title):
    for i in movie_data.data:
        if title in i['title_rus']:
            yield f'Название фильма {i["title_rus"]},\nРежиссёр - {i["director"]},\nДата выхода на экраны - {i["year"]},\nЖанр - {i["genre"]}'

def search_director(director):
    for i in movie_data.data:
        if director in i["director"]:
            yield f'{i["title_rus"]}, режиссёр - {i["director"]}' #,\nДата выхода на экраны - {i["year"]},\nЖанр - {i["genre"]}'

def search_year(year):
    for i in movie_data.data:
        if year in i['year']:
            yield f'{i["title_rus"]} - {i["year"]}' #  \nРежиссёр - {i["director"]},\nДата выхода на экраны - {i["year"]},\nЖанр - {i["genre"]}'

def search_genre(genre):
    for i in movie_data.data:
        if genre in i['genre']:
            yield f'{i["title_rus"]}'#, жанр - {i["genre"]}'