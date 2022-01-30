import bcrypt

class Encrypt:
    def __init__(self) -> None:
        pass

    def get_hashed_password(self, plain_text_password: str) -> str:
        # Hash a password for the first time
        #   (Using bcrypt, the salt is saved into the hash itself)
        bytes_password = bytes(plain_text_password, 'utf-8')
        return bcrypt.hashpw(bytes_password, bcrypt.gensalt())

    def check_password(self, plain_text_password: str, hashed_password: bytes) -> bool:
        # Check that an unencrypted password matches one that has
        # previously been hashed
        bytes_password = bytes(plain_text_password, 'utf-8')
        return bcrypt.checkpw(bytes_password, hashed_password)

if __name__ == '__main__':
    enc = Encrypt()
    enc_psd = enc.get_hashed_password('Hello')
    print(enc_psd)

    enc_psd = enc.get_hashed_password('Hello')
    print(enc_psd)
    dec_psd = enc.check_password('Hello', enc_psd)
    print(dec_psd)
