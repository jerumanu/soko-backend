# from app.v1 import v1_api

from flask_restx import Namespace, fields

class RegisterDto():
        api = Namespace('user', description=' user related operations')
        user = api.model('user', {
                'email': fields.String(required=True, description=' user email address'),
                'username': fields.String(required=True, description='user username'),
                'password': fields.String(required=True, description='user password'),
        })
class LoginDto():
        api = Namespace('login', description='login related operations')
        login = api.model('login', {
                'email': fields.String(required=True, description='user email address'),
                'password': fields.String(required=True, description='user password'),
        })
class LogoutDto():
        api = Namespace('logout', description='logout related operations')
        logout= api.model('logout', {
                'refresh_token': fields.String(required=True, description='refresh token'),
        })
class ResteTokenDto():
        api = Namespace('token', description='refresh token related operations')
        token= api.model('token', {
                'refresh_token': fields.String(required=True, description='refresh token'),
        })
class ResetPasswordDto():
        api = Namespace('reset', description='reste pasword related operations')
        reset= api.model('reset', {
                'email': fields.String(required=True, description='user email address'),
                'old_password': fields.String(required=True, description='user old password'),
                'new_password': fields.String(required=True, description='user new password'),
        })


