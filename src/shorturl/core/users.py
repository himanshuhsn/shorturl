from logging import exception
from .. import config
from ..utils import keygenerator
from ..utils import encrypt
from flask import jsonify

from ..model.model import User
from ..model.model import db

key_object = keygenerator.KeyGenerator()
encrypt = encrypt.Encrypt()

def create_user(body):
    #check if already exists
    try:
        users = User.query.filter_by(username=body.username).all()
    except Exception as e:
        return(str(e))
    # print("user ", users)
    if len(users) != 0:
        return None
    # get the api_key for this user
    key_object.generateKey(10)
    dev_key = key_object.getKey()
    # get the quota from config.py
    quota = config.ALLOWED_API_CALL_PER_MONTH
    # encrypt password
    encrypted_password = encrypt.get_hashed_password(body.password) 
    # insert item into user table
    try:
        new_user = User(
                username = body.username,
                email = body.email,
                password = encrypted_password,
                key = dev_key,
                quota = quota
        )
        db.session.add(new_user)
        db.session.commit()
        return "User added. username ={}".format(new_user.username)
    
    except Exception as e:
        return(str(e))

def get_key(username, password):
    # check username and password
    # try:
    #     users = User.query.filter_by(username=username).all()
    #     if len(users) != 0:
    #         # check password
    #         if encrypt.check_password(password, users.password) == False:
    #             return "Wrong password \n"
    #         # get the item from user table using username
    #         else:
    #             return jsonify(users.serialize())['key']
    #     else:
    #         return None
    # except Exception as e:
	#     return(str(e))
    pass

def update_key(username, password):
    # check username and password
    # get a new key
    # update the key to user table
    pass

def update_user(username, body):
    # check username and password
    # get the hashed of new password
    # update the user table with the new password
    pass