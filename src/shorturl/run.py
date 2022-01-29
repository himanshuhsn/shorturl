import os
from flask_migrate import Migrate
import connexion

from .web import encoder

from .config import SQLALCHEMY_DATABASE_URI

from .model.model import db

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

# def create_app():
#     print("db2 ", db)
#     db.create_all()
#     print("db3 ", db)
#     flask_app.json_encoder = encoder.JSONEncoder
#     return flask_app