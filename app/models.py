from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class Book:

    def __init__(self,id,title,author,book_description,thumbnail,webReaderLink):

        self.id =id
        self.author = author
        self.title = title
        self.book_description = book_description
        self.thumbnail = thumbnail
        self.webReaderLink = webReaderLink
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


    def __repr__(self):
        return f'user {self.username}'

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    book_id = db.Column(db.String)
    book_title = db.Column(db.String)
    image_path = db.Column(db.String)
    book_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_review(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(book_id=id).all()
        return reviews







