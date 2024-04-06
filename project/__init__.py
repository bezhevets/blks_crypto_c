from flask import Flask

from project.extensions import db, migrate
from project.views import main


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app
