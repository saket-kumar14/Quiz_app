from flask import request, current_app as app
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required
from models import *
from datetime import datetime



class WelcomeAPI(Resource):
    @jwt_required()
    def get(self):
        print(request)
        print(get_jwt().get('role'))
        print(get_jwt_identity())
        return {'message': 'Welcome to the API'}, 200
    
    def post(self):
        msg = f'Welcome {request.get_json.get("f_name")}'
        return {'message': msg}, 200
    
class LoginAPI(Resource):
    def post(self):
        data = request.json
        if not (data.get('email') and data.get('password')):
            return {'error': 'Both fields are required'}, 400
        user = Users.query.filter_by(email=data.get('email')).first()
        if not user: 
            return {'error': 'User not found'}, 400
        if user.password != data.get('password'):
            return {'error': 'Incorrect credentials'}, 401
        token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})

        return {'message': f'Welcome {user.f_name}',
                'access_token': token,
                'user_name' : user.f_name,
                'role' : user.role}, 200       
            
        
    
class SignupAPI(Resource):
    def post(self):
        data = request.json
        if not (data.get('f_name') and data.get('l_name') and data.get('email') and data.get('password') and data.get('dob') and data.get('role')):
            return {'error': 'All fields are required'}, 400
        
        if not (2 <= len(data.get('f_name').strip()) <= 60):
            return {'error': 'First name should be between 2-60 characters'}, 400
        if not (2 <= len(data.get('l_name').strip()) <= 60):
            return {'error': 'Last name should be between 2-60 characters'}, 400

        if not (5 <= len(data.get('email').strip()) <= 60):
            return {'error': 'Email should be between 5-60 characters'}, 400

        password = data.get('password').strip()
        if ' ' in password:
            return {'error': 'Password should not contain spaces'}, 400
        if not (8 <= len(password) <= 60):
            return {'error': 'Password should be between 8-60 characters'}, 400

        try:
            dob_obj = datetime.strptime(data.get('dob'), '%d-%m-%Y').date()
        except ValueError:
            return {'error': 'Date of birth should be in DD-MM-YYYY format'}, 400


        if data['role'] not in ['user', 'admin']:
            return {'error': 'Role should be either user or admin'}, 400

        if Users.query.filter_by(email=data.get('email')).first():
            return {'error': 'User already exists'}, 400
        
        new_user = Users(f_name=data.get('f_name').strip(), l_name=data.get('l_name').strip(), 
                         email=data.get('email').strip(), password=data.get('password').strip(), 
                         dob=dob_obj, role=data.get('role'))
        
        db.session.add(new_user)
        db.session.commit()
        return{'message': 'User Created'}, 201
        
        
class SubjectAPI(Resource):
    @jwt_required()
    def post(self):
        if get_jwt().get('role') != 'admin':
            return {'error': 'Only admin can create subjects'}, 401

        data = request.json
        if not (data.get('name') and data.get('description')):
            return {'error': 'All fields are required'}, 400
        
        if not (2 <= len(data.get('name').strip()) <= 50):
            return {'error': 'Name should be between 2-50 characters'}, 400
        
        if not (2 <= len(data.get('description').strip()) <= 255):
            return {'error': 'Description should be between 2-255 characters'}, 400
        
        if Subject.query.filter_by(name=data.get('name')).first():
            return {'error': 'Subject already exists'}, 400
        
        new_subject = Subject(name=data.get('name').strip(), description=data.get('description').strip())

        db.session.add(new_subject)
        db.session.commit()
        return{'message': 'Subject Created'}, 201
    
