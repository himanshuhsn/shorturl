import os

ALLOWED_API_CALL_PER_MONTH = os.environ['ALLOWED_API_CALL_PER_MONTH']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
DATABASE = os.environ['DATABASE']
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'