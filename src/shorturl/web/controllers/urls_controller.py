import connexion

from ..models.create_url_obj import CreateUrlObj  # noqa: E501
from ..models.short_url_obj import ShortUrlObj  # noqa: E501

from ...core import urls
from flask import redirect


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
    if return_data == "WRONG_API_KEY":
        return {"error" : "WRONG_API_KEY"}, 406
    elif return_data == "CUSTOM_ALIAS_ALREADY_EXISTS":
        return {"error": "CUSTOM_ALIAS_ALREADY_EXISTS"}, 406
    elif return_data == "LIMIT_EXCEEDED":
        return {"error": return_data}, 403
    elif return_data == "SHORT_URL_EXPIRED":
        return {"error": return_data}, 406
    elif return_data == "SHORT_URL_DOES_NOT_EXISTS":
        return {"error": return_data},406
    elif return_data != None:
        return {"short_url" : return_data}, 200
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
    long_url = urls.redirect_url(shorturl)
    if long_url == "SHORT_URL_EXPIRED":
        return {"error": long_url}, 404
    elif long_url == "SHORT_URL_DOES_NOT_EXISTS":
        return {"error": long_url},404
    elif long_url == None:
        return {}, 404
    else:    
        if long_url[:7] == "http://":
            long_url = long_url[7:]
        elif long_url[:8] == "https://":
            long_url = long_url[8:]
        try:
            return redirect("https://"+long_url),303
        except:
            return redirect("http://"+long_url),303