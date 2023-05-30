from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['production'])
    config['production'].init_app(app)
    db.init_app(app)

    return app
