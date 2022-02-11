import hashlib
import time
import base64

class URLGenerator:
    '''
    Generates constant length (= 7) string for short url.
    '''
    def __init__(self) -> None:
        pass

    def encode(self, api_dev_key: str, longurl: str) -> str:
        usernameWithLongurl = api_dev_key + longurl + str(time.time())
        md5encodedUrl=base64.b64encode(hashlib.md5(usernameWithLongurl.encode('utf-8')).digest()).decode("utf-8")
        return md5encodedUrl[:7]

if __name__ == '__main__':
    urlGen = URLGenerator()
    print( urlGen.encode('dev_key_1', 'www.google.com') )
    print( urlGen.encode('dev_key_2', 'www.yahoo.com') )
    print( urlGen.encode('dev_key_3', 'www.facebook.com') )