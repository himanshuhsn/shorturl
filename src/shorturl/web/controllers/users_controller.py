import connexion
import six

from ..models.key import Key  # noqa: E501
from ..models.login import Login  # noqa: E501
from ..models.update_user import UpdateUser  # noqa: E501
from ..models.user import User  # noqa: E501
from ..models.user_data import UserData  # noqa: E501
from .. import util


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_key_by_name(username):  # noqa: E501
    """Delete key by the user name

    This can only be done by the logged in user. # noqa: E501

    :param username: The username for which key is to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_key_by_name(username):  # noqa: E501
    """Get key by user name

    This can only be done by the logged in user. # noqa: E501

    :param username: The username for which key is to be fetched.
    :type username: str

    :rtype: Key
    """
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: UserData
    """
    return 'do some magic!'


def login_user(body):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param body: Login user
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Login.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

    This can only be done by the logged in user. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_key_by_name(username, body):  # noqa: E501
    """Update key by user name

    This can only be done by the logged in user. # noqa: E501

    :param username: The username for which is key is to be updated.
    :type username: str
    :param body: Updated key object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Key.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user(username, body):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be updated
    :type username: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
