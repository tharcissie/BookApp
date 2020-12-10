
from flask import render_template,request,redirect, url_for,abort
from . import main
from ..request import get_books, get_book
from flask_login import login_required,current_user
from .forms import UpdateProfile,ReviewForm
from .. import db,photos
from ..models import User,Review
import markdown2

@main.route('/')
def index():
    science = get_books('science')
    print(science)
    computers = get_books('computers')
    fiction = get_books('fiction')
    romantic = get_books('romantic')
    title = 'Home - Welcome to The best Books Website Online'
    return render_template('index.html',title = title,science = science,computers = computers,fiction = fiction,romantic = romantic)


    
@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)  


@main.route('/user/<name>/update',methods = ['GET','POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',name=user.username))

    return render_template('profile/update.html',form =form)      


@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))    

@main.route('/book/<id>')
def book(id):
    '''
    View book page function that returns the book details page and its data
    '''
    book = get_book(id)
    title = 'Book'
    book_reviews = Review.get_reviews(book.id)
    print(book_reviews)
    return render_template('book.html',title = title,book = book,new_book=book_reviews)

@main.route('/book/review/new/<id>/', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    book = get_book(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        # Updated review instance
        new_review = Review(book_id=book.id,book_title=title,image_path=book.thumbnail,book_review=review,user=current_user)
        # save review method
        new_review.save_review()
        return redirect(url_for('.book',id = book.id ))

    title = f'{book.title} review'
    return render_template('new_review.html',title = title, review_form=form, book=book)


@main.route('/review/<id>/')
def single_review(id):
    review=Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(review.book_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)