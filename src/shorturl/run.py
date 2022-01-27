import os
from venv import create
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Index

import connexion

from .web import encoder

abs_file_path = os.path.abspath(os.path.dirname(__file__))
openapi_path = os.path.join(abs_file_path, "../", "../", "openapi")
app = connexion.FlaskApp(
    __name__, specification_dir=openapi_path, options={"swagger_ui": True, "serve_spec": True}
)
app.add_api("specification.yml", strict_validation=True)
flask_app = app.app

from config import SQLALCHEMY_DATABASE_URI
flask_app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)

class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    key = db.Column(db.String(), nullable=False)
    quota = db.Column(db.Integer, nullable=False)

    def __init__(self, username, email, password, key, quota):
        self.username = username
        self.email = email
        self.password = password
        self.key = key
        self.quota = quota

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'key': self.key,
            'quota': self.quota
        }

class Shorturl(db.Model):
    __tablename__ = 'shorturls'

    shorturl = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, ForeignKey('users.username'))
    longurl = db.Column(db.String)
    expiry = db.Column(db.DateTime)

    __table_args__ = (Index('find_shorturl_index', "username", "longurl"), )

    def __init__(self, shorturl, longurl, username, expiry):
        self.shorturl = shorturl
        self.longurl = longurl
        self.username = username
        self.expiry = expiry

    def serialize(self):
        return {
            'shorturl': self.shorturl, 
            'longurl': self.longurl,
            'username': self.username,
            'expiry': self.expiry
        }

db.create_all()
flask_app.json_encoder = encoder.JSONEncoder

def create_app():
    return flask_app