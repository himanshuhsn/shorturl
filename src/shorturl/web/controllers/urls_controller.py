import connexion
import six

from ..models.create_url_obj import CreateUrlObj  # noqa: E501
from ..models.short_url_obj import ShortUrlObj  # noqa: E501
from .. import util


def create_url(api_key, body):  # noqa: E501
    """Generate a short url for a long url.

    Generate a short url for a long url. # noqa: E501

    :param api_key: api key for generating short url
    :type api_key: str
    :param body: 
    :type body: dict | bytes

    :rtype: ShortUrlObj
    """
    if connexion.request.is_json:
        body = CreateUrlObj.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def redirect_url(shorturl):  # noqa: E501
    """Redirects to long url.

     # noqa: E501

    :param shorturl: shorturl for the fetching the corresponding long url
    :type shorturl: str

    :rtype: None
    """
    return 'do some magic!'
