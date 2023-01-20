import sys
import unittest
sys.path.insert(0, 'd:/Code/goodreads_statistics/')
from src.utils.openlibrary_api import OpenlibraryAPI

class TestGenre(unittest.TestCase):

    @staticmethod
    def test_get_genre_by_isbn():
        elantris_isbn = "0765350378"
        elantris_genre = OpenlibraryAPI.get_genre_by_isbn(elantris_isbn)
        assert elantris_genre == "Fantasy"

    @staticmethod
    def test_get_genre_by_title():
        conversations_title = "Conversations with Friends"
        conversations_genre = OpenlibraryAPI.get_genre_by_title(conversations_title)
        assert conversations_genre == "Fiction"

if __name__ == '__main__':
    unittest.main()
    print("Openlibrary API test PASSED")