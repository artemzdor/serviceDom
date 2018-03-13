from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DBDOM.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
# app.config.from_pyfile('config.py')
from app import views, models
db.create_all()