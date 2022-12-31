import logging
from flask import request
from flask_restx import Resource,Namespace
from validate_email import validate_email
from app.main.auth.extensions import  auth
from app.main.auth.models.user  import User
from app.main.auth.extensions.auth.jwt_auth  import refresh_jwt
# from app.main.auth.utils.auth_dto import register_model, login_model, \
#     refresh_token_model,logout_model, rest_password_model
from app.main.auth.views.user_views import  save_new_user
from app.main.auth.views.auth_views import  Auth
from app.errors import CustomFlaskErr as notice

from ..utils.auth_dto import RegisterDto


api = RegisterDto.api
_user = RegisterDto.user


@api.route('/register')
class RegisterRequired(Resource):
    """register interface"""
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)

    def post(self):
        data = request.json
        
        return save_new_user(data=data)    

        