from logging import exception
from .. import config
from ..utils import keygenerator
from ..utils import encrypt
from flask import jsonify

from ..model.model import User
from ..model.model import db

key_object = keygenerator.KeyGenerator()
encrypt = encrypt.Encrypt()

def verify_password(given_password, saved_hashed_password):
    return encrypt.check_password(given_password, bytes(saved_hashed_password,"utf-8"))

def create_user(body):
    #check if already exists
    try:
        users = User.query.filter_by(username=body.username).all()
    except Exception as e:
        return(str(e))
    if len(users) != 0:
        return None
    # get the api_key for this user
    key_object.generateKey(10)
    dev_key = key_object.getKey()
    # get the quota from config.py
    quota = config.ALLOWED_API_CALL_PER_MONTH
    # encrypt password
    encrypted_password = encrypt.get_hashed_password(body.password).decode('utf8') 
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
        return dev_key
    except Exception as e:
        return(str(e))

def get_key(username, password):
    # check username and password
    try:
        users = User.query.filter_by(username=username).first()
        if users != None:
            # check password
            if verify_password(password, users.password) == True:
                # get the item from user table using username   
                return users.key
            else:
                return None
        else:
            return None
    except Exception as e:
	    return(str(e))

def update_key(username, password):
    # check username and password
    try:
        users = User.query.filter_by(username=username).first()
        if users != None:
            # check password
            if verify_password(password, users.password):
                # get a new key
                key_object.generateKey(10)
                dev_key = key_object.getKey()   
                # update the key to user table
                updated_user = User.query.filter_by(username = username).first()
                updated_user.key = dev_key
                db.session.commit()
                return dev_key
            else:
                return None
        else:
            return None
    except Exception as e:
	    return(str(e))
    

def update_user(username, body, password):
    # check username and password
    try:
        users = User.query.filter_by(username=username).first()
        if users != None:
            # check password
            if verify_password(password, users.password):
                # get the hashed of new password 
                new_encrypted_password = encrypt.get_hashed_password(body.newpassword).decode('utf8')
                # update the user table with the new password
                updated_user = User.query.filter_by(username = username).first()
                updated_user.password = new_encrypted_password
                db.session.commit()    
                return "Password updated successfully"
            else:
                return None
        else:
            return None
    except Exception as e:
	    return(str(e))