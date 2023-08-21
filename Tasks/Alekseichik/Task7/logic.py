import sqlite3

def conn_cur():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT,director TEXT, year INTEGER, genre TEXT)''')
    connection.commit()
    return connection, cursor
    
def commit_close(connection):
    connection.commit()
    connection.close()

def add_new(title,director,year,genre):
    connection, cursor = conn_cur()
    cursor.execute('''INSERT INTO movies(title,director,year,genre) 
                   VALUES (?,?,?,?)''',(title,director,year,genre))
    commit_close(connection)
    return 'Media successfully ADDED'

def get_all():
    connection, cursor = conn_cur()
    data = cursor.execute('SELECT * FROM movies').fetchall()
    connection.close()
    for row in data:
        yield('  '.join(str(item) for item in row))
    
def search_title(title):
    connection, cursor = conn_cur()
    data = cursor.execute('''SELECT * FROM movies WHERE title LIKE ?''',
                          ('%' + title + '%',)).fetchall()
    if len(data) < 1:
        raise TimeoutError
    else:
        for row in data:
            yield row
    connection.close()


def search_director(director):
    connection, cursor = conn_cur()
    data = cursor.execute('''SELECT * FROM movies WHERE director LIKE ?''',
                          ('%' + director + '%',)).fetchall()
    if len(data) < 1:
        raise TimeoutError
    else:
        for row in data:
            yield row
    connection.close()

def search_year(year):
    connection, cursor = conn_cur()
    data = cursor.execute('''SELECT * FROM movies WHERE year LIKE ?''',
                          ('%' + year + '%',)).fetchall()
    if len(data) < 1:
        raise TimeoutError
    else:
        for row in data:
            yield row
    connection.close()

def search_genre(genre):
    connection, cursor = conn_cur()
    data = cursor.execute('''SELECT * FROM movies WHERE genre LIKE ?''',
                          ('%' + genre + '%',)).fetchall()
    if len(data) < 1:
        raise TimeoutError
    else:
        for row in data:
            yield row
    connection.close()

def to_find_duplicate():
    connection, cursor = conn_cur()
    data = cursor.execute('SELECT * FROM movies').fetchall()
    connection.close()
    return data

