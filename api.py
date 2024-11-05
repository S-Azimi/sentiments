from flask import Blueprint

from . import database

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/apps")
def get_app_list():
    apps = database.get_all_apps()
    return apps


@bp.route("/apps/<int:app_id>")
def get_app_info(app_id):
    app_info = database.get_app_info(app_id)
    return app_info
