import connexion
import six

from ..models.favorite_url_list_obj import FavoriteUrlListObj  # noqa: E501
from ..models.mark_favorite_obj import MarkFavoriteObj  # noqa: E501
from .. import util
from ...core import favorite


def get_favorite(api_key = None):  # noqa: E501
    """Get favorite urls by user name

    Get favorite urls by user name # noqa: E501

    :param api_key: api key of user
    :type api_key: str

    :rtype: FavoriteUrlListObj
    """
    if connexion.request.headers['api_key']:
        key = connexion.request.headers['api_key']

    return_data = favorite.get_favorite(key)

    if return_data == "WRONG_API_KEY":
        return {"error" : []},400
    return {"favorite_list" : return_data},200


def mark_favorite(body, api_key = None):  # noqa: E501
    """Mark an existing url as favorite

    Mark an existing url as favorite # noqa: E501

    :param api_key: api key for marking short url as favorite
    :type api_key: str
    :param shorturl: Shorturl to be marked favorite
    :type shorturl: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MarkFavoriteObj.from_dict(connexion.request.get_json())  # noqa: E501

    if connexion.request.headers['api_key']:
        key = connexion.request.headers['api_key']

    return_data = favorite.mark_favorite(key, body)
    if return_data == "WRONG_KEY":
        return {"error" : return_data}, 406
    elif return_data == "WRONG_SHORT_URL":
        return {"error" : return_data}, 406
    return {"status" : return_data}, 200
