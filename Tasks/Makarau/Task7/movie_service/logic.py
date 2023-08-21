import json

with open ("movies.json", 'r') as f:
    data = json.load(f)

def add_movie(title,director,year,genre):
    counter = 0
    for i in data:
        if i["title"] == title and i["director"] == director and i["year"] == year and i["genre"] == genre:
            counter+=1
    if counter == 0:
        data.append({'title':title,'director':director,'year':year,'genre':genre})
        res = "The movie was added"
    else:
        res = "This movie has been added before"         
    with open ("movies.json", 'w') as f:
        json.dump(data,f, indent=2)               
    return res     
    
def get_all_movies():
    try:    
        for i in data:
            yield (f'\ntitle: {i["title"]}\ndirector: {i["director"]}\nyear: {i["year"]}\ngenre: {i["genre"]}')
    except RuntimeError:
        raise RuntimeError ("An error occurred while getting data about all movies")

def search_title(title):
    for i in data:
        if i["title"] == title:
            yield (f'\ntitle: {i["title"]}\ndirector: {i["director"]}\nyear: {i["year"]}\ngenre: {i["genre"]}')        
        
def search_director(director):
    for i in data:
        if i["director"] == director:
            yield (f'\ntitle: {i["title"]}\ndirector: {i["director"]}\nyear: {i["year"]}\ngenre: {i["genre"]}')

def search_year(year):
    for i in data:
        if i["year"] == year:
            yield (f'\ntitle: {i["title"]}\ndirector: {i["director"]}\nyear: {i["year"]}\ngenre: {i["genre"]}')

def search_genre(genre):
    for i in data:
        if i["genre"] == genre:
            yield (f'\ntitle: {i["title"]}\ndirector: {i["director"]}\nyear: {i["year"]}\ngenre: {i["genre"]}')