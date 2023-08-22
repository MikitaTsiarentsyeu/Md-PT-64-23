import sqlite3
from contextlib import contextmanager

@contextmanager
def connection():
    conn = sqlite3.connect('m_coll.db')
    yield conn
    conn.close()


def init_db():
    with connection() as cursor:
        cursor.execute ('''CREATE TABLE IF NOT EXISTS movie_collection
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        director TEXT,
                        year INT,
                        genre TEXT);''')


def add_movie(title, director,year,genre):
    with connection() as cursor:
        cursor.execute('INSERT INTO movie_collection (title, director, year, genre) VALUES (?,?,?,?)', (title, director,year, genre) )
        cursor.commit()


def search_title(title):
    with connection() as cursor:
        row = cursor.execute('SELECT * FROM movie_collection WHERE title LIKE ?',(title,))
        for i in row:
            yield i


def search_director(director):
    with connection() as cursor:
        row = cursor.execute('SELECT * FROM movie_collection WHERE director LIKE ?', (director,))
        for i in row:
            yield i


def search_year(year):
    with connection() as cursor:
        row = cursor.execute('SELECT * FROM movie_collection WHERE year = ?', (year,))
        for i in row:
            yield i


def search_genre(genre):
    with connection() as cursor:
        row = cursor.execute('SELECT * FROM movie_collection WHERE genre LIKE ?', (genre,))
        for i in row:
            yield i


def movie_list():
    with connection() as cursor:
        rows = cursor.execute('SELECT * FROM movie_collection').fetchall()
        for i in rows:
            yield i
