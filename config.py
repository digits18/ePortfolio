import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv('Database_URL', 'postgresql://neondb_owner:OXgGf2qvjER3@ep-wispy-shape-a4os0v66-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False