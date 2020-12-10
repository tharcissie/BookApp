
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField, TextAreaField,ValidationError,RadioField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Book review')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')