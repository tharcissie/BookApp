import unittest
from app.models import Book
Book = Book

class BookTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_book = Book(123,'corneille','le cid','french book','http://books.google.com/books/content?id=iyovDAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','http://play.google.com/books/reader?id=iyovDAAAQBAJ&hl=&printsec=frontcover&source=gbs_api')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_book,Book))