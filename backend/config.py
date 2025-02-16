import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQL_ALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')