import connexion
import six

from .. import util


def home_url():  # noqa: E501
    """Home to shorturl services.

     # noqa: E501


    :rtype: None
    """
    return {"response" : "Welcome to shorturl services", "UI-path" : "/ui"}, 200
