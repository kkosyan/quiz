from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import config
from .main import main as main_blueprint

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['production'])
    config['production'].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
