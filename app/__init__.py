from flask import Flask
from .config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_SORT_KEYS'] = False
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Instantiate Flask-Migrate library here
migrate = Migrate(app,db)

from app import views
