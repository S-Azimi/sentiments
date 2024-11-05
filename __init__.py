from flask import Flask
from . import config

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



def create_app():
    my_app = Flask(__name__, instance_relative_config=True)
    my_app.config.from_object(config.Config)
    db.init_app(my_app)
    from . import api
    my_app.register_blueprint(api.bp)
    return my_app
