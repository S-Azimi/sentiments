from . import db


class Application(db.Model):
    __tablename__ = "app_info"
    app_id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String)
    app_name_company = db.Column(db.String)
    app_img_base64 = db.Column(db.String)
    app_version = db.Column(db.String)
    app_total_rate = db.Column(db.String)
    app_average_rate = db.Column(db.String)
    app_install = db.Column(db.String)
    app_category = db.Column(db.String)
    app_size = db.Column(db.String)
    app_last_update = db.Column(db.String)
    app_url = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.app_id,
            "name": self.app_name,
            "company": self.app_name_company,
            "version": self.app_version,
            "totalRate": self.app_total_rate,
            "averageRate": self.app_average_rate,
            "install": self.app_install,
            "category": self.app_category,
            "size": self.app_size,
            "lastUpdate": self.app_last_update,
            "url": self.app_url,
            "img": self.app_img_base64,
        }

    def __repr__(
        self,
    ):  # just used to debuge the output of object and see the content of obj
        return f"<Application {self.app_name}>"

