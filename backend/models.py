from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer,Date, Boolean, ForeignKey
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    f_name = Column(String(80), nullable=False)
    l_name = Column(String(80), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    dob = Column(Date, nullable=False)
    role = Column(String(10), nullable=False, default = "user")
    is_admin = Column(Boolean, nullable=False, default=False)
    is_user = Column(Boolean, nullable=False, default=False)
    #Relationships
    quizzes = db.relationship('Quiz', backref='users',cascade="all, delete-orphan", lazy='select')
    
class Subject(db.Model):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    #Relationships
    chapters = db.relationship('Chapter', backref='subject', cascade="all, delete-orphan", lazy='select')

class Chapter(db.Model):
    __tablename__ = 'chapter'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(255), nullable=False)
    #Foreign key
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    #Relationships
    quizzes = db.relationship('Quiz', backref='chapter', cascade="all, delete-orphan", lazy='select')



class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    date_of_quiz = Column(Date, nullable=False)
    time_duration = Column(Integer, nullable=False)
    remarks = Column(String(255), nullable=False)
    #Foreign key
    chapter_id = Column(Integer, ForeignKey('chapter.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    #Relationships
    questions = db.relationship('Questions', backref='quiz', cascade="all, delete-orphan", lazy='select')
    scores = db.relationship('Scores', backref='quiz', cascade="all, delete-orphan", lazy='select')

class Questions(db.Model):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String(255), nullable=False)
    option1 = Column(String(255), nullable=False)
    option2 = Column(String(255), nullable=False)
    option3 = Column(String(255), nullable=False)
    option4 = Column(String(255), nullable=False)
    #Foreign key
    quiz_id = Column(Integer, ForeignKey('quiz.id'), nullable=False)   


class Scores(db.Model):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True)
    total_score = Column(Integer, nullable=False)
    total_time = Column(Integer, nullable=False)
    correct = Column(Integer, nullable=False)
    wrong = Column(Integer, nullable=False)
    performance = Column(String(50), nullable=False)
    #Foreign key
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quiz.id'), nullable=False)