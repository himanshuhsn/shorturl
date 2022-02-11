from distutils.command.config import config
from ..utils.urlgenerator import URLGenerator
from ..model.model import User
from ..model.model import Shorturl
from ..model.model import db
from datetime import datetime, timedelta
from ..config import TIME_FRAME, ALLOWED_API_CALL, DEFAULT_EXPIRY
import time

url_object = URLGenerator()

def check_api_key_user(api_key, short_url):
    try:
        user = User.query.filter_by(key=api_key).first()
    except Exception as e:
        return(str(e))
    try:
        urls = Shorturl.query.filter_by(shorturl=short_url).first()
    except Exception as e:
        return(str(e))
    if user and urls and user.username == urls.username:
        return True
    return False

def check_api_key(api_key):
    try:
        user = User.query.filter_by(key=api_key).first()
        if user is not None:
            return True
        return False
    except Exception as e:
        return(str(e))

def check_quota(api_key, period):
    if period <= 0:
        return "PERIOD_INVALID"

    try:
        row_last_expire_time = User.query.filter_by(key=api_key).first()
    except Exception as e:
        return(str(e))

    cur_time = int(time.time())

    last_expire_time = row_last_expire_time.last_exp_time

    if cur_time-last_expire_time < period:
        return True

    batch_diff = int(( cur_time-last_expire_time ) // period)

    updated_exp_time_in_utc = last_expire_time + (batch_diff)*period

    try:
        row_last_expire_time.last_exp_time = updated_exp_time_in_utc - 1
        row_last_expire_time.quota = ALLOWED_API_CALL
        db.session.commit()
    except Exception as e:
        return(str(e))

    return True

def check_username(username, api_key):
    try:
        user = User.query.filter_by(key=api_key).first()
        if user.username == username:
            return True
        return False
    except Exception as e:
        return str(e)

def create_url(body,api_key):
    #check api_key
    if not check_api_key(api_key):
        return "WRONG_API_KEY"

    # check correct username
    if not check_username(body.username, api_key):
        return "WRONG_USER_NAME"

    # check if user is allowed
    check_quota(api_key, TIME_FRAME)
    
    #parsing time_to_live
    if body.time_to_live == '':
        expiry = int(time.time()) + DEFAULT_EXPIRY
    else:
        expiry = int(time.time()) + int(body.time_to_live)

    #parsing custom_alias
    if body.custom_alias == '':
        short_url = url_object.encode(api_key, body.long_url)
    else:
        # check if customurl already exists
        if validate_url(body.custom_alias):
            return "CUSTOM_ALIAS_ALREADY_EXISTS"
        short_url = body.custom_alias

    # inserting item into shorturls table
    # add the url to the shorturl table
    try:
        if validate_url(short_url):
            return "URL_EXIST"
        else:
            new_url = Shorturl(
                shorturl = short_url,
                username = body.username,
                longurl = body.long_url,
                expiry = expiry
            )
            db.session.add(new_url)
            db.session.commit()

            # decrease user quota
            try:
                updated_user = User.query.filter_by(username = body.username).first()
                if updated_user.quota == 0:
                    return "KEY_QUOTA_EXPIRED"
                updated_user.quota -= 1
                db.session.commit() 
            except Exception as e:
                return str(e)
            return new_url.shorturl
    except Exception as e:
        return(str(e))

def validate_url(shorturl):
    try:
        urls = Shorturl.query.filter_by(shorturl=shorturl).first()
        if urls is not None:
            return True
        return False
    except Exception as e:
        return(str(e))


def delete_url(api_key, shorturl):
    # validate the api_key
    if not check_api_key_user(api_key, shorturl):
        return "WRONG_API_KEY_OR_URL_DOES_NOT_EXISTS"

    # check if url exists 
    if validate_url(shorturl) == None:
        return "SHORT_URL_DOES_NOT_EXISTS"
    else:
        # delete the shorturl
        try:
            Shorturl.query.filter_by(shorturl=shorturl).delete()
            db.session.commit()
            return "Url deleted"
        except Exception as e:
            return str(e)
    

def redirect_url(shorturl):
    # check if url exists or not
    if validate_url(shorturl) == None:
        return "SHORT_URL_DOES_NOT_EXISTS"
    # get the long url from short url
    try:
        query_object = Shorturl.query.filter_by(shorturl=shorturl).first()
        cur_time = time.time()
        if(int(cur_time) > query_object.expiry):
            return "SHORT_URL_EXPIRED"
        url = query_object.longurl
        return url
    except Exception as e:
        return None
    