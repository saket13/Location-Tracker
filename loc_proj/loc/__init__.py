from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 

from flask_googlemaps import GoogleMaps


app= Flask(__name__)


import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyA8wstQYK-Fkski2FxKI1FxKZgpq1gjcYk"

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category = 'info'

# Initialize the extension
gm=GoogleMaps(app)

from loc import routes
