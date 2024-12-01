from flask import Flask
from .routes import bp
from .models import db, migrate
from .models import migrate
from config import Config
import logging


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)
    # app.config['SECRET_KEY'] = 'gugyueguieqwgyguhgahgsajiGHU'
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nature_db.sqlite"
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    app.register_blueprint(bp)

    # Setup console logging
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('OladimejiSanni-iPorfolio Startup')
    return app
