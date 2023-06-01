import pandas as pd
from src.utils.openlibrary_api import *

# class Book:
#     """
#     Class Book holds the information of a book.
#     """

#     def __init__(self, title=None, author=None, isbn=None, date_start=None, date_end=None,
#                  my_rating=None, average_rating=None, num_pages=None) -> None:

#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.genre = OpenlibraryAPI.get_genre_by_isbn(isbn)
#         self.my_rating = my_rating
#         self.average_rating = average_rating
#         self.date_start = date_start
#         self.date_end = date_end
#         self.num_pages = num_pages

#     def __repr__(self) -> str:
#         return self.title + " - " + self.author

class Bookshelf:
    """
    Class Bookshelf holds all the books in the database.
    """

    def __init__(self, goodreads_csv=None) -> None:

        self.books = pd.read_csv(goodreads_csv, usecols=['Title', 'Author', 'ISBN', 'Date Added',
                                 'Date Read', 'My Rating', 'Average Rating', 'Number of Pages'])

        self.books['Genre'] = self.books.apply(lambda x: OpenlibraryAPI.get_genre(x), axis=1)

        print("Imported " + str(len(self.books)) + " books from file '" + goodreads_csv + "'")

    def get_books_by_genre(self, genre=None):
        return self.books[self.books['Genre'] == genre]

