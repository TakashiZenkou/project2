from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,FileField,PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed,FileRequired

class UserForm(FlaskForm):

    username = StringField('username',validators=[InputRequired()]) 
    password = PasswordField('password',validators=[InputRequired()])
    fullname = StringField('fullname',validators=[InputRequired()])
    email = StringField('email',validators=[InputRequired()])
    location = StringField('location',validators=[InputRequired()])
    biography = StringField('bio',validators=[InputRequired()])
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg','png'])])



