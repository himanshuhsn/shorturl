from ..model.model import User
from ..model.model import Shorturl
from ..model.model import db

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


def mark_favorite(api_key, body): 
    # verify api_key
    if not check_api_key(api_key):
        return "WRONG_API_KEY"

    # match usernames from both the tables
    if not check_api_key_user(api_key, body.shorturl):
        return "WRONG_SHORT_URL"

    # get markFavorite value from body
    try:
        # mark/unmark shorturl in shorturls table 
        updated_url = Shorturl.query.filter_by(shorturl = body.shorturl).first()
        if body.markfavorite == "0":
            updated_url.favorite = False
        else:
            updated_url.favorite = True
        db.session.commit()
        return "SUCCESS"
    except Exception as e:
        return str(e)



def get_favorite(api_key):
    # verify api_key
    if not check_api_key(api_key):
        return "WRONG_API_KEY"

    # get username from api_key in user table
    try:
        user = User.query.filter_by(key=api_key).first()
        username = user.username
    except Exception as e:
        return(str(e))

    # query urls for all the urls marked as favorite of username
    # return list of favorite urls
    try:
        favorite_list = Shorturl.query.filter_by(username=username, favorite = True).all()
        favorite_shorturl = [url.shorturl for url in favorite_list]
        return favorite_shorturl
    except Exception as e:
        return(str(e))