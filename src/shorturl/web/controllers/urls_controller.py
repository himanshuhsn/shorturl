import connexion
import six

from ..models.url import Url  # noqa: E501
from .. import util


def create_url(body):  # noqa: E501
    """Generate a short url for a long url.

    Generate a short url for a long url. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Url.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def redirect_url(shorturl):  # noqa: E501
    """Redirects to long url.

    Redirects to long url. # noqa: E501

    :param shorturl: shorturl for the fetching the corresponding long url
    :type shorturl: str

    :rtype: None
    """
    return 'do some magic!'
