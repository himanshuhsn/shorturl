import hashlib

class URLGenerator:
    '''
    Generates constant length (= 7) string for short url.
    '''
    def __init__(self) -> None:
        pass

    def encode(self, api_dev_key: str, longurl: str) -> str:
        usernameWithLongurl = api_dev_key + longurl
        md5encodedUrl = hashlib.md5(usernameWithLongurl.encode('utf-8')).hexdigest()
        return md5encodedUrl[:7]

if __name__ == '__main__':
    urlGen = URLGenerator()
    print( urlGen.encode('dev_key_1', 'www.google.com') )
    print( urlGen.encode('dev_key_2', 'www.yahoo.com') )
    print( urlGen.encode('dev_key_3', 'www.facebook.com') )