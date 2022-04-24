"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import json
from app import app,db,login_manager
from flask import render_template, request, jsonify, send_file,redirect, url_for, flash, g , session
import os
from .models import Cars,Users,Favourites
from .forms import UserForm,LoginForm,CarForm
from werkzeug.utils import secure_filename
from datetime import *
from flask_wtf.csrf import generate_csrf
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
import jwt
from functools import wraps
from flask import _request_ctx_stack
import datetime



###
# Routing for your application.
###

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None) 

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated


@app.route('/api/secure', methods=['GET'])
@requires_auth
def api_secure():
    # This data was retrieved from the payload of the JSON Web Token
    # take a look at the requires_auth decorator code to see how we decoded
    # the information from the JWT.
    user = g.current_user
    return jsonify(data={"user": user}, message="Success")


@app.route('/')
def index():
    return send_file(os.path.join('../dist/', 'index.html'))

@app.route('/api/register',methods = ["POST"])
def register():
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')
    form = UserForm()
    if request.method == "POST" and form.validate_on_submit():

        picture = request.files['photo']
        filename = secure_filename(picture.filename)
        picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        username = request.form['username']
        password = request.form['password']
        name = request.form['fullname']
        email = request.form['email']
        location = request.form['location']
        biography = request.form['biography']
        date_joined = date.today()
        photo = filename

        reg = Users(username,password,name,email,location,biography,photo,date_joined) 

        db.session.add(reg)
        db.session.commit()

        return jsonify({"message": 'User Registration Successful'})
        
    return jsonify(form_errors(form))

@app.route('/api/csrf-token',methods=["GET"])
def get_csrf():
    return jsonify({'csrf_token' : generate_csrf()})

@app.route("/api/auth/login", methods=["POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = Users.query.filter_by(username = username).first()
            print(user)
            if user is not None and check_password_hash(user.password,password):
                session['userid'] = user.id
                token = jwt.encode({
                    'sub': user.email,
                    'iat': datetime.datetime.now(datetime.timezone.utc),
                    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)},
                    os.path.join(app.config['SECRET_KEY']))    

                return jsonify(message=" Login Successful and Token was Generated",data={"token":token},id={"id":user.id})         
            else:
                return jsonify({"message": 'User Login Unsuccessful'})
    return jsonify(form_errors(form))
 


@app.route('/api/auth/logout', methods=['POST'])
@requires_auth
def logout():
    session.clear()
    user = g.current_user
    return jsonify(data={"user": user}, message="Logged Out")



@app.route("/api/cars", methods = ['POST','GET'])
@requires_auth
def pcars():
    form = CarForm()
    if request.method == 'POST':
        if form.validate_on_submit():
                make = request.form['Make']
                model = request.form['Model']
                color = request.form['Colour']
                year = request.form['Year']
                price = request.form['Price']
                cartype = request.form['CarType']
                transmission = request.form['Transmission']
                description = request.form['Description']
                picture = request.files['photo']
                filename = secure_filename(picture.filename)
                picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                user_id = request.form['user_id']
                car = Cars(description,make,model,color,year,transmission,cartype,price,filename,user_id)
                db.session.add(car)
                db.session.commit()
                return jsonify({"message": 'Car Registration Successful'}), 201
    if request.method == 'GET':
        cars3 = []
        cars = db.session.query(Cars).all()
        x = abs(len(cars)-3)
        for i in range(len(cars)-1,x-1,-1):
            car = {"id":cars[i].id, "photo":cars[i].photo , "year": cars[i].year, "make": cars[i].make,"price":cars[i].price, "model":cars[i].model, "description":cars[i].description, "colour":cars[i].colour, "transmission": cars[i].transmission, "car_type": cars[i].car_type, "user_id": cars[i].user_id}
            cars3.append(car)
        return jsonify(cars3)
    return jsonify(errors = form_errors(form))

            
       


@app.route('/api/cars/<car_id>',methods = ["GET"])
@requires_auth
def car(car_id):
    if request.method == "GET":
        car = db.session.query(Cars).filter_by(id=car_id).first()
        if car:
            return jsonify(car)
        return jsonify({"message": 'Car with that id does not exist'}), 400



@app.route('/api/cars/<car_id>/favourite', methods = ['POST'])
@requires_auth
def favcar(car_id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        carid = request.form['car_id']
        favorite = Favourites.query.filter_by(car_id = carid).first()
        if favorite is None:
            fav = Favourites(carid,user_id)
            db.session.add(fav)
            db.session.commit()
            return jsonify(message="Car successfully added to Favourites"), 200
        return jsonify(message="Already favourited this car"), 200


#Search Route
"""
Search by make or model
"""
@app.route('/api/search', methods=['GET'])
@requires_auth
def search():
    try:
        make = request.args.get('make')
        model = request.args.get('model')
        cars = Cars.query.filter((Cars.make == make) | (Cars.model == model)).all()
        if not cars:
            return jsonify({"message":"No Cars Matching the Search Terms Were Found"})
        return jsonify(cars)
    except Exception as d:
        print(d)
        return jsonify({"message":"Internal Server Error"}), 500

#User ID Route
"""
Get details of a user by id
"""
@app.route('/api/users/<user_id>', methods=['GET'])
@requires_auth
def users(user_id):
    if int(user_id) == session.get('userid'):
        user = Users.query.filter_by(id=user_id).first()
        return jsonify(id=user.id, username=user.username, name=user.name, email=user.email, location=user.location, biography=user.biography, photo=user.photo, date_joined=user.date_joined.strftime("%B %d, %Y"))
    else:
        return jsonify({"message":"Unauthorized"}), 401


#User Favorites Route
"""
Get cars that a user has favorited
"""
@app.route('/api/users/<user_id>/favourites', methods=['GET'])
@requires_auth
def userfavorites(user_id):
    print()
    if int(user_id) == session.get('userid'):
        favorites = Favourites.query.filter_by(user_id=user_id).all()
        cars = []
        for favorite in favorites:
            cars.append(Cars.query.filter_by(id=favorite.car_id).first())
        return jsonify([car.serialize() for car in cars])
    else:
        return jsonify({"message":"Unauthorized"}), 401


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")