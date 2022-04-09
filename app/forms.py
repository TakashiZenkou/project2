from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,FileField,PasswordField,TextAreaField,DecimalField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed,FileRequired

class UserForm(FlaskForm):

    username = StringField('username',validators=[InputRequired()]) 
    password = PasswordField('password',validators=[InputRequired()])
    fullname = StringField('fullname',validators=[InputRequired()])
    email = StringField('email',validators=[InputRequired()])
    location = StringField('location',validators=[InputRequired()])
    biography = StringField('bio',validators=[InputRequired()])
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg','png'],'Images')])

class LoginForm(FlaskForm):

    username = StringField('username',validators=[InputRequired()]) 
    password = PasswordField('password',validators=[InputRequired()])


class CarForm(FlaskForm):	

	description = TextAreaField('Description',[InputRequired()])
	make = StringField('Make',[InputRequired()])
	model = StringField('Model',[InputRequired()])
	colour = StringField('Colour',[InputRequired()])
	year = StringField('Year', [InputRequired()])
	transmission = StringField('Transmission', [InputRequired()])
	car_type = StringField('Car Type', [InputRequired()])
	price = DecimalField('Price',[InputRequired()])
	photo = FileField('Photo',validators = [FileRequired(),FileAllowed(['jpg','png'],'Images')])