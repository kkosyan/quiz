from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import configure_uploads, IMAGES, UploadSet

from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()
images = UploadSet('images', IMAGES)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['production'])
    config['production'].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    configure_uploads(app, images)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
