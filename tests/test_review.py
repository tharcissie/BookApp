import unittest
from app.models import Review,User
from app import db

class ReviewTest(unittest.TestCase):

    def setUp(self):

            self.user_wecode = User(username = 'developer',password = '12345', email = 'deve@gmail.com')
            self.new_review = Review(book_id=12345,book_title='Review for books',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",book_review='This book is the best thing since sliced bread',posted='2020-10-21T13:28:15Z',user = self.user_wecode )
    def tearDown(self):
        
            Review.query.delete()
            User.query.delete()
    def test_check_instance_variables(self):

            self.assertEquals(self.new_review.book_id,12345)
            self.assertEquals(self.new_review.book_title,'Review for books')
            self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
            self.assertEquals(self.new_review.book_review,'This book is the best thing since sliced bread')
            self.assertEquals(self.new_review.posted,'2020-10-21T13:28:15Z')
            self.assertEquals(self.new_review.user,self.user_wecode)

    def test_save_review(self):
            self.new_review.save_review()
            self.assertTrue(len(Review.query.all())>0)
    def test_get_review_by_id(self):
            self.new_review.save_review()
            got_reviews = Review.get_reviews(12345)
            self.assertTrue(len(got_reviews) == 1)