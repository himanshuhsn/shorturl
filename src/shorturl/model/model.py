from sqlalchemy import ForeignKey, Index
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

    shorturl = db.Column(db.String, primary_key=True)
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
