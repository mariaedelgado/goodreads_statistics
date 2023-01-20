import json
from urllib.request import urlopen

def get_genre_by_isbn(book_isbn):
    # Connect to Google Books API, which allows to retrieve genre by the ISBN of the book
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    api_request = urlopen(api + book_isbn)

    google_book = json.load(api_request)
    book_info = google_book["items"][0]["volumeInfo"]
    return book_info["categories"]

def get_isbn_by_title(book_title):
    # Connect to Google Books API, which allows to retrieve genre by the ISBN of the book
    api = "https://www.googleapis.com/books/v1/volumes?q="
    print(api+book_title)
    api_request = urlopen(api + book_title)

    return json.load(api_request)