import os
from flask_migrate import Migrate
import connexion
import time
from sqlalchemy import delete

from apscheduler.schedulers.background import BackgroundScheduler

from .web import encoder

from .config import SQLALCHEMY_DATABASE_URI, TABLE_CLEAN_PERIOD

from .model.model import db, Shorturl

abs_file_path = os.path.abspath(os.path.dirname(__file__))
openapi_path = os.path.join(abs_file_path, "../", "../", "openapi")
app = connexion.FlaskApp(
    __name__, specification_dir=openapi_path, options={"swagger_ui": True, "serve_spec": True}
)
app.add_api("specification.yml", strict_validation=True)
flask_app = app.app

flask_app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(flask_app)
migrate = Migrate(flask_app, db)

with flask_app.app_context():
    db.create_all()

def url_table_clean_job():
    cur_time = int(time.time())
    try:
        with flask_app.app_context():
            rows = Shorturl.query.filter(Shorturl.expiry <= cur_time).delete()
            db.session.commit()
    except Exception as e:
        print(str(e))
        return(str(e))

scheduler = BackgroundScheduler()
job = scheduler.add_job(url_table_clean_job, 'interval', seconds=TABLE_CLEAN_PERIOD)
scheduler.start()

# def create_app():
#     print("db2 ", db)
#     db.create_all()
#     print("db3 ", db)
#     flask_app.json_encoder = encoder.JSONEncoder
#     return flask_app