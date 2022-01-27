import os
import random


class URLGenerator:
    '''
    Generates a constant length (len = 10) base 62 encoded url for given integer.
    Encoded value should not be predictable
    Append random bytes to end of the integer then encode
    '''
    def __init__(self) -> None:
        self.base62_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def base62encode(self, long_URL_counter: int) -> str:
        hash_string = ''
        while long_URL_counter > 0:
            hash_string += self.base62_string[long_URL_counter % 62]
            long_URL_counter //= 62
        return hash_string

    def encode(self, number: int) -> str:
        # get assigned number from counter for the url
        number_to_bytes = number.to_bytes(6, 'big')

        # append 2 random bytes at end
        appended_bytes = number_to_bytes + os.urandom(2)
        changed_number = int.from_bytes(appended_bytes, 'big')

        # encode the counter
        short_URL_variable_chars = self.base62encode(changed_number)
        short_URL = self.make_len_const(short_URL_variable_chars, 10)
        
        return short_URL

    def make_len_const(self, variable_chars_string: str, limit: int) -> str:
        more_char_to_add = limit - len(variable_chars_string)
        const_chars_string = variable_chars_string + ''.join(random.choices(self.base62_string, k=more_char_to_add))
        return const_chars_string

if __name__ == '__main__':
    urlGen = URLGenerator()
    urlGen.encode(0)
    urlGen.encode(1000)
    urlGen.encode(3521614606208)