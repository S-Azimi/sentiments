import psycopg2
import os
from flask import current_app
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


def get_db_connection():
    return psycopg2.connect(
        database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port
    )


def db_select(query, *params):

    con = get_db_connection()
    cur = con.cursor()
    cur.execute(query, *params)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data


def get_all_apps():
    query = "select app_id, app_name from app_info order by app_name"
    apps = db_select(query=query)
    for app in apps:
        print(app[0])
    return apps


def get_all_apps2():
    with current_app.app_context():
        from . import db
        from . import models

        apps = db.session.execute(db.select(models.Application)).scalars()
        return apps


def get_app_info(app_id):
    query = "select app_id, app_name,  from app_info where app_id = %s"
    app_info = db_select(query, [app_id])
    return app_info


if __name__ == "__main__":
    print("running")
    get_all_apps()
