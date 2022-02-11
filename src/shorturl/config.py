import os

# Times are in seconds
ALLOWED_API_CALL = eval(os.environ['ALLOWED_API_CALL'])
TIME_FRAME = eval(os.environ['TIME_FRAME'])
TABLE_CLEAN_PERIOD = eval(os.environ['TABLE_CLEAN_PERIOD'])
DEFAULT_EXPIRY = eval(os.environ['DEFAULT_EXPIRY'])

USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
DATABASE = os.environ['DATABASE']
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'