import json
repo_name = "repo.json"

try:
    with open(repo_name, 'r') as f:
        repo = json.load(f)
except:
    raise RuntimeError("An error occured while accessing a storage")

def add_article(title, author, year, issue):
    article = {}
    article = {"title": title, "author": author, "year": year, "issue": issue}
    if article not in repo:
        repo.append(article)
        res = "The article was added"
    else:
        res = "The article already exists"
    with open(repo_name, 'w') as f:
        json.dump(repo, f)
    return res



def get_all_articles():
    try:
        count = 1
        res = []
        for i in repo:
            res.append(f'{count}-{i["title"]}')
            count += 1
    except:
        raise RuntimeError("An error occured during getting all articles, please try again")
    return res

def search_title(title):
    count = 0
    for i in repo:
        if title in i["title"]:
            count +=1
            yield f'{count}. Article_title - {i["title"]}\nauthor - {i["author"]}\nyear - {i["year"]}\nissue - {i["issue"]}'

def search_author(author):
    count = 0
    for i in repo:
        if author in i["author"]:
            count += 1
            yield f'{count}. Article_title - {i["title"]}\nauthor - {i["author"]}\nyear - {i["year"]}\nissue - {i["issue"]}'

def search_year(year):
    count = 0
    for i in repo:
        if year in i["year"]:
            count += 1
            yield f'{count}. Article_title - {i["title"]}\nauthor - {i["author"]}\nyear - {i["year"]}\nissue - {i["issue"]}'

def search_issue(issue):
    count = 0
    for i in repo:
        if issue in i["issue"]:
            count += 1
            yield f'{count}. Article_title - {i["title"]}\nauthor - {i["author"]}\nyear - {i["year"]}\nissue - {i["issue"]}'