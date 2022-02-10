# time-parameter are in seconds

ALLOWED_API_CALL = 5
TIME_FRAME = 30
TABLE_CLEAN_PERIOD = 5
DEFAULT_EXPIRY = 100

USER='postgres'
PASSWORD='somePassword'
HOST='172.18.0.1'
PORT='5432'
DATABASE='shorturl'

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'