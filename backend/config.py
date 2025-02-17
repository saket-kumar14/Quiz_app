import os
from datetime import timedelta

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'
    JWT_SECRET_KEY = "my_secret"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    PASSWORD_HASH = 'sha512'