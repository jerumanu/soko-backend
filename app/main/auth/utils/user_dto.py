# from app.main import api
from flask_restx import fields, reqparse,Namespace

class DeleteUser():
        api = Namespace('delete', description=' user related operations')
        delete = api.model('delete', {
                'email': fields.String(required=True, description='user email address'),
                'username': fields.String(required=True, description='user username'),
                'password': fields.String(required=True, description='user password'),
        })

class Userlist():
        api = Namespace('users', description=' user related operations')
        users = api.model('users', {
                'email': fields.String(required=True, description='user email address'),
                'user_role': fields.String(required=True, description='user user_role'),
                # 'is_active': fields.String(required=True, description='user is_active'),
                'mobile': fields.String(required=True, description='user mobile'),
                'about_me': fields.String(required=True, description='user info'),
                'public_id': fields.String(description='user Identifier'),
                'member_since': fields.String(required=True, description='user register time'),
        })

