from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import *
import os
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///form.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize the app with the extension
app.config["SECRET_KEY"] = 'anything you want'

db.init_app(app)



from forms.user import routes




