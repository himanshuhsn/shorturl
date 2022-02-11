import connexion
import six

from ..models.api_key_obj import ApiKeyObj  # noqa: E501
from ..models.updated_user import UpdatedUser  # noqa: E501
from ..models.user import User  # noqa: E501
from ..models.api_key_obj import ApiKeyObj
from .. import util

from ...core import users


def create_user(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: User object for creating new user.
    :type body: dict | bytes

    :rtype: ApiKeyObj
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    
    return_data = users.create_user(body)
    if return_data != None:
        return {"api_key" : return_data}, 200
    else:
        return {"error" : "USERNAME_ALREADY_EXISTS"}, 406


def get_key(username, password = None):  # noqa: E501
    """Get key by user name

     # noqa: E501

    :param username: The username for which key is to be fetched.
    :type username: str
    :param password: 
    :type password: str

    :rtype: ApiKeyObj
    """
    password = connexion.request.headers['password']
    return_data = users.get_key(username, password)
    if return_data != None:
        return {"api_key" : return_data}, 200
    else:
        return {}, 400


def update_key(username, password = None):  # noqa: E501
    """Update current key with a new generated key

     # noqa: E501

    :param username: The username for which api key is to be updated.
    :type username: str
    :param password: 
    :type password: str

    :rtype: ApiKeyObj
    """
    password = connexion.request.headers['password']
    return_data = users.update_key(username, password)
    if return_data != None:
        return {"api_key" : return_data}, 200
    else:
        return {}, 400


def update_user(username, body, password = None):  # noqa: E501
    """Update user

     # noqa: E501

    :param username: 
    :type username: str
    :param password: 
    :type password: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdatedUser.from_dict(connexion.request.get_json())  # noqa: E501
    password = connexion.request.headers['password']
    return_data = users.update_user(username, body, password)
    if return_data != None:
        return {}, 200
    else:
        return {}, 400
