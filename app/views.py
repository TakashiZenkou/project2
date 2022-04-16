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
from .forms import UserForm,LoginForm
from werkzeug.utils import secure_filename
from datetime import *
from flask_wtf.csrf import generate_csrf
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
import jwt
from functools import wraps



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
    return jsonify(message="This is the beginning of our API")

@app.route('/api/register',methods = ["POST"])
def register():

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
            if user is not None and check_password_hash(user.password,password):
                session['userid'] = user.id
                token = jwt.encode({
                    'sub': user.email,
                    'iat': datetime.now(),
                    'exp': datetime.now() + timedelta(minutes=30)},
                    os.path.join(app.config['SECRET_KEY']))    

                return jsonify(message=" Login Successful and Token was Generated",data={"token":token})         
            else:
                return jsonify({"message": 'User Login Unsuccessful'})
    return jsonify(form_errors(form))
 


@app.route('/api/auth/logout', methods=['POST'])
@requires_auth
def logout():
    user = g.current_user
    return jsonify(data={"user": user}, message="Logged Out")


#Search Route
"""
Search by make or model
"""
@app.route('/api/search', methods=['GET'])
def search():
    pass

#User ID Route
"""
Get details of a user by id
"""
@app.route('/api/users/{user_id}', methods=['GET'])
def users(user_id):
    pass

#User Favorites Route
"""
Get cars that a user has favorited
"""
@app.route('/api/users/{user_id}/favourites', methods=['GET'])
def userfavorites(user_id):
    pass


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