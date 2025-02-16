from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.sql import *
from datetime import *

db = SQLAlchemy()

class User(db.Model):
    _tablename_ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)



class Subject(db.Model):
    _tablename_ = 'subject'
    id = Column(Integer, primary_key=True)
    subj_name = Column(String(80), unique=True, nullable=False)