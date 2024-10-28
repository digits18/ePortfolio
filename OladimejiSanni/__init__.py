from flask import Flask
from .routes import bp
from .models import db
from .models import migrate


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = 'gugyueguieqwgyguhgahgsajiGHU'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nature_db.sqlite"
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    app.register_blueprint(bp)
    return app