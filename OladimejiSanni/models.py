from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Contact(db.Model):
    tablename = 'contact'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String, nullable=False, unique=True)
    subject = db.Column(db.String, nullable=False, unique=False)
    message = db.Column(db.String, nullable=False, unique=False)

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def __repr__(self):
        return self.email
