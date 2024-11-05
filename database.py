from . import db
from . import models

# Define all needed queries

def get_all_apps():
    apps = db.session.query(models.Application).all()
    return [app.to_dict() for app in apps]


def get_app_info(app_id):
    app = db.session.query(models.Application).get(app_id)
    if app:
        return app.to_dict()
    return "error", 404
