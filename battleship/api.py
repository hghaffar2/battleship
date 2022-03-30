from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    from .views.battleship import ship
    app.register_blueprint(ship)

    return app
