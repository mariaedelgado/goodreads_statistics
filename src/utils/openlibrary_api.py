import json
from urllib.request import urlopen

# Define list of main genres to be used. The retrieved 'subject' list from the API contains
# several sub-genres, so we are going to do a comparison to get the main ones. TBD.
__genres_list = ['Fantasy', 'Romance', 'Science-Fiction', 'History']

class OpenlibraryAPI():
    """
    Class OpenlibraryAPI to access to missing data of the books. For instance, genre is
    not provided in the Goodreads export, and it's a parameter we want to obtain.
    """

    @classmethod
    def get_genre(self, book=None):

        genre, error = OpenlibraryAPI.get_genre_by_isbn(book['ISBN'])

        if not error:
            return genre
        
        genre, error = OpenlibraryAPI.get_genre_by_title(book['Title'])

        if not error:
            return genre
        else:
            return 'Undefined'

    def get_genre_by_isbn(self, isbn=None):
        api = "http://openlibrary.org/search.json?isbn="
        api_request = urlopen(api + str(isbn))

        try:
            openlibrary_book = json.load(api_request)
            subjects = openlibrary_book["docs"][0]["subject"]
            return pick_genre_from_subject_list(subjects), None

        except Exception as error:
            return None, error

    def get_genre_by_title(self, title=None):
        api = "http://openlibrary.org/search.json?title="
        title = str(title).lower().replace(" ","+")
        api_request = urlopen(api + title)

        try:
            openlibrary_book = json.load(api_request)
            subjects = openlibrary_book["docs"][0]["subject"]
            return pick_genre_from_subject_list(subjects), None

        except Exception as error:
            return None, error


def pick_genre_from_subject_list(subject_list):
    for genre in __genres_list:
        if genre in subject_list:
            return genre

    return subject_list[0]