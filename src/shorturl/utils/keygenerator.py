import secrets

class KeyGenerator:
    def __init__(self) -> None:
        self.key = ''

    def generateKey(self, length: int) -> None:
        self.key = secrets.token_urlsafe(length)

    def getKey(self) -> str:
        self.generateKey(32)
        return self.key

if __name__ == '__main__':
    keyGen = KeyGenerator()
    key = keyGen.getKey()
    print(key)