import connexion

from ..models.create_url_obj import CreateUrlObj  # noqa: E501
from ..models.short_url_obj import ShortUrlObj  # noqa: E501

from ...core import urls


def create_url(body, api_key=None):  # noqa: E501
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
    if connexion.request.headers['api_key']:
        key = connexion.request.headers['api_key']

    return_data = urls.create_url(body,key)
    if return_data != None:
        return return_data, 200
    else:
        return {}, 406



def delete_url(shorturl, api_key = None):  # noqa: E501
    """Deletes the short url

    # noqa: E501

    :param api_key: api key for deleting shorturl
    :type api_key: str
    :param shorturl: shorturl for deleting the shorturl
    :type shorturl: str

    :rtype: None
    """
    if connexion.request.headers['api_key']:
        key = connexion.request.headers['api_key']
    return_data = urls.delete_url(key, shorturl)
    print(return_data)
    if return_data != None:
        return {"Success" : return_data}, 200
    else:
        return {}, 406


def redirect_url(shorturl):  # noqa: E501
    """Redirects to long url.

     # noqa: E501

    :param shorturl: shorturl for the fetching the corresponding long url
    :type shorturl: str

    :rtype: None
    """
    return_data = urls.redirect_url(shorturl)
    if return_data != None:
        return return_data, 200
    else:
        return {}, 406