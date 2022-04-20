from . import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash

@dataclass
class Cars(db.Model):

    id: int
    description: str
    make: str
    model: str
    colour: str
    year: str
    transmission: str
    car_type: str
    price: float
    photo: str
    user_id: int

    __tablename__ = 'Cars'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    colour = db.Column(db.String(100))
    year = db.Column(db.String(100))
    transmission = db.Column(db.String(100))
    car_type = db.Column(db.String(100))
    price = db.Column(db.Float(10,2))
    photo = db.Column(db.String(100))
    user_id = db.Column(db.Integer)

    def serialize(self):
        return {
            'id':self.id,
            'description':self.description,
            'year': self.year,
            'make': self.make,
            'model': self.model,
            'colour': self.colour,
            'transmission':self.transmission,
            'car_type':self.car_type,
            'price':self.price,
            'photo':self.photo,
            'user_id':self.user_id
        }

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.id)

    def __init__(self,description,make,model,colour,year,transmission,car_type,price,photo,user_id):
        self.description = description
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = user_id

class Favourites(db.Model):

    __tablename__ = 'Favourites'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.id)

    def __init__(self,car_id,user_id):
        self.car_id = car_id
        self.user_id = user_id

class Users(db.Model):

    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique = True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    location = db.Column(db.String(100))
    biography = db.Column(db.String(100))
    photo = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime)	

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

    def __init__(self,username,password,name,email,location,biography,photo,date_joined):
        self.username = username
        self.password = generate_password_hash(password,method='pbkdf2:sha256')
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_joined = date_joined






