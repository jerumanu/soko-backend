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

from ..utils.auth_dto import RegisterDto,LoginDto,LogoutDto




api=LoginDto.api
_login = LoginDto.login

# api =LogoutDto.api
# _logout = LogoutDto.logout

# auth_ns = Namespace('auth')

# parser = auth_ns.parser()
# parser.add_argument('Authorization',
#                     type=str,
#                     required=True,
#                     location='headers',
#                     help='Bearer Access Token')


######  API
# @api.route('/register')
# class RegisterRequired(Resource):
#     """register interface"""
#     @api.response(201, 'User successfully created.')
#     @api.doc('create a new user')
#     @api.expect(_user, validate=True)

#     def post(self):
#         data = request.json
        
#         return save_new_user(data=data)

@api.route('/login')
class LoginRequired(Resource):
    """登录接口"""
    @api.doc('user login')
    @api.expect(_login , validate=True)
    def post(self):
        post_data = request.json
        print(post_data)
        return Auth.login_user(data=post_data)

@api.route('/logout')
class Logout(Resource):
    """登出接口"""
    @api.doc('logout a user')
    # @auth.login_required
    def post(self):
        post_data = request.json
        return Auth.logout(data=post_data)

@api.route('/refresh_token')
class RefreshTokenRequired(Resource):
    """刷新Token"""
    @api.doc('refress token ')
    def post(self):
        post_data = request.json
        return Auth.refresh_token(data=post_data)

@api.route('/confirm/<confirm_token>', endpoint="confirm")
class ConfirmRquired(Resource):
    """登录接口"""

    @api.doc('User email confirmation')
    # @api.expect(login_model, validate=True)
    @api.param('email', required=True)
    def get(self, confirm_token):

        # Get Confirm email
        confirm_email = request.args.get('email')

        # Check confirm email
        #if  validate_email(confirm_email, check_mx=True, verify=True):

        #    return {"message": "email invalid input."}, 423
        # use staticmethod verify confirm toke
        if User.verify_confirm_token(confirm_token, confirm_email):

            raise notice(status_code=200, return_code=30002,action_status=True)

        else:

            raise notice(status_code=202,return_code=20009, action_status=False)



# # ###################
# # # RestPasswordRequired
# # ##############################
# RestPasswordRequired
###################
# @api.route('/change_password')
# class RestPasswordRequired(Resource):
#     """重置密码"""
#     @api.doc('rest password')
#     # @auth_ns.doc(parser=parser)
#     @api.expect(rest_password_model, validate=True)
#     # @auth_ns.param('email',location='body',required=True)
#     # @auth_ns.param('new_password',location='body',required=True)

#     def put(self):
#         pass

# #######

# @auth_ns.route('/change_email')
# class RestPasswordRequired(Resource):
#     """更改邮箱"""

#     # @auth_ns.doc(parser=parser)
#     @auth_ns.expect(rest_password_model, validate=True)
#     # @auth_ns.param('email',location='body',required=True)
#     # @auth_ns.param('new_password',location='body',required=True)

#     def put(self):
#         pass


# # ###################
# # RefreshTokenRequired
# # ###################

# @auth_ns.route('/refresh_token')

# class RefreshRequired(Resource):
#     """登录接口"""
#     @auth_ns.doc('refresh token')
#     # @auth_ns.doc(parser=parser)
#     @auth_ns.expect(rest_password_model, validate=True)
#     # @auth_ns.param('email',location='body',required=True)
#     # @auth_ns.param('new_password',location='body',required=True)

#     def put(self):
#         pass

