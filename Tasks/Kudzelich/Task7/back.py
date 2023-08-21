import json
repo_name = "repo.json"

try:
    with open(repo_name, 'r', encoding='utf-8') as f:
        repo = json.load(f)
except:
    raise RuntimeError("An error occured while accessing a storage")

def add_movie(title, director, year, genre):
    movie = {}
    movie = {"title": title, "director": director, "year": year, "genre": genre}
    if movie not in repo:
        repo.append(movie)
        res = "The movie was added"
    else:
        res = "The movie already exists"
    with open(repo_name, 'w', encoding='utf-8') as f:
        json.dump(repo, f)

    return res

def get_all_movies():
    try:
        count = 1
        res = []
        for i in repo:
            res.append(f'{count}-{i["title"]}')
            count += 1
    except:
        raise RuntimeError("An error occured during getting all movies, please try again")
    return res

def search_title(title):
    count = 0
    for i in repo:
        if title in i["title"]:
            count +=1
            yield f'{count}. Название фильма - {i["title"]}\nРежиссёр - {i["director"]}\nГод выхода - {i["year"]}\nЖанр - {i["genre"]}'

def search_director(director):
    count = 0
    for i in repo:
        if director in i["director"]:
            count += 1
            yield f'{count}. Название фильма - {i["title"]}\nРежиссёр - {i["director"]}\nГод выхода - {i["year"]}\nЖанр - {i["genre"]}'

def search_year(year):
    count = 0
    for i in repo:
        if year in i["year"]:
            count += 1
            yield f'{count}. Название фильма - {i["title"]}\nРежиссёр - {i["director"]}\nГод выхода - {i["year"]}\nЖанр - {i["genre"]}'

def search_genre(genre):
    count = 0
    for i in repo:
        if genre in i["genre"]:
            count += 1
            yield f'{count}. Название фильма - {i["title"]}\nРежиссёр - {i["director"]}\nГод выхода - {i["year"]}\nЖанр - {i["genre"]}'