from logging import exception
from sqlite3 import IntegrityError

from sqlalchemy import UniqueConstraint
from .. import config
from ..utils import keygenerator
from ..utils import encrypt
from flask import jsonify
from ..utils.urlgenerator import URLGenerator

from ..model.model import User
from ..model.model import Shorturl
from ..model.model import db
import shorturl
from datetime import datetime, timedelta

url_object = URLGenerator()

def create_url(body,api_key):
    # validate the api_key
    # add the url to the shorturl table
    try:
        users = User.query.filter_by(key=api_key).first()
    except Exception as e:
        return(str(e))
    # inserting item into shorturls table
    if body.time_to_live == '':
        expiry = datetime.utcnow() + timedelta(days=1)
    else:
        expiry = datetime.utcnow() + timedelta(seconds=int(body.time_to_live))
    if body.custom_alias == '':
        short_url = url_object.encode(api_key,body.long_url)
    else:
        short_url = body.custom_alias
    try:
        new_url = Shorturl(
                shorturl = short_url,
                username = body.username,
                longurl = body.long_url,
                expiry = expiry
        )
        db.session.add(new_url)
        db.session.commit()
        return "Url added. url ={}".format(new_url.shorturl)
    except Exception as e:
        return(str(e))

def validate_url(surl):
    try:    
        users = Shorturl.query.filter_by(shorturl=surl).all()
        return users
    except Exception as e:
        return(str(e))


def delete_url(api_key, shorturl):
    # validate the api_key
    
    # delete the shorturl
    pass

def redirect_url(shorturl):
    # get the long url from short url
    pass