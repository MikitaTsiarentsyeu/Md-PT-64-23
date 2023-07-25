import os
p = os.path.join('Md-PT-64-23', 'Tasks', 'Korotkevich', 'Task7')
os.chdir(p)

import json
films = 'films.json'
directors = 'directors.json'
years = 'years.json'
genres = 'genres.json'

with open(films, 'r') as f:
    title_dict = json.load(f)
with open(directors, 'r') as f:
    director_dict = json.load(f)
with open(years, 'r') as f:
    year_dict = json.load(f)
with open(genres, 'r') as f:
    genre_dict = json.load(f)

def add_film(title, director, year, genre):
    if title not in title_dict:
        title_dict[title] = [director, year, genre]
    else:
        return('Something wrong')
    with open(films, 'w') as f:
        json.dump(title_dict, f)
    if director not in director_dict:
        director_dict[director] = [title]
    else:
        director_dict[director].append(title)
    with open(directors, 'w') as f:
        json.dump(director_dict, f)
    if year not in year_dict:
        year_dict[year] = [title]
    else:
        year_dict[year].append(title)
    with open(years, 'w') as f:
        json.dump(year_dict, f)
    if genre not in genre_dict:
        genre_dict[genre] = [title]
    else:
        genre_dict[genre].append(title)
    with open(genres, 'w') as f:
        json.dump(genre_dict, f)

def get_all_film():
    return '\n'.join([f'{title:} : {", ".join(title_dict[title])}' for title in title_dict])

def search(dict_json, key):
    data = dict_json[key]
    if len(data) == 1:
        return f'{key} : {data}'
    else:
        return f'{key} : {", ".join(data)}'  

def search_title(key): 
    data = title_dict[key]
    return f'{key} : {", ".join(data)}'

def search_director(key):
    return search(director_dict, key)

def search_year(key):
    return search(year_dict, key)

def search_genre(key):
    return search(genre_dict, key)