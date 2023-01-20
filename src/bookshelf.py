from utils.openlibrary_api import *

class Book:
    """
    Class Book holds the information of a book.
    """

    def __init__(self, title=None, author=None, isbn=None, date_start=None, date_end=None, my_rating=None, average_rating=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = get_genre_by_isbn(isbn)
        self.my_rating = my_rating
        self.average_rating = average_rating
        self.date_start = date_start
        self.date_end = date_end

# class Bookshelf:
#     """"
#     Class Bookshelf holds all the books in the database.
#     """"