from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager


from models import *
from config import *
from api import *

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

app.app_context().push()

def add_admin():
    admin = Users.query.filter_by(role='admin').first()
    if not admin:
        admin = Users(f_name='admin' , l_name ='admin' , email='admin@gmail.com', password='admin123', dob=datetime.now(),role='admin', is_admin=True)
        db.session.add(admin)
        db.session.commit()
        return "Admin Created"

@app.route('/')
def index():
    return "Hello World"

api.add_resource(WelcomeAPI, '/api/welcome')
api.add_resource(LoginAPI, '/api/login')
api.add_resource(SignupAPI, '/api/signup')
api.add_resource(SubjectAPI, '/api/subject')



if __name__ == '__main__':
    db.create_all()
    add_admin()
    app.run(debug=True)