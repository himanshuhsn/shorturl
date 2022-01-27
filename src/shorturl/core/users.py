from .. import config

def create_user(body):
    # get the api_key for this user
    # get the quota from config.py
    # insert item into user table
    pass

def get_key(username, password):
    # check username and password
    # get the item from user table using username
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
