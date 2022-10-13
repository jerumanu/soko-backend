# from app import db
from flask import request
from app.main import db
from app.main.auth.models.user import User
from app.main.auth.models.blacklist  import Blacklist
from .user_views import  save_changes
from app.main.auth.extensions.auth.jwt_auth import refresh_jwt
from app.errors import CustomFlaskErr as notice
from validate_email import validate_email



class Auth:
    @staticmethod
    def login_user(data):
        try:
            # Get user email and password.
            email, password = data.get('email').strip(), data.get('password').strip()

        except Exception as why:

            # Log input strip or etc. errors.
            # logging.info("Email or password is wrong. " + str(why))
            # Return invalid input error.
            return {'message': "invaild mail or password"}, 404

        #if not validate_email(data['email'],verify=True,check_mx=True):
         #   raise error(status_code=500,return_code=20006)    

        # Check if user information is none.
        if email is None or password is None:
            return {'message': "invaild mail or passworg"}, 404

        # Get user if it is existed.
        user = User.query.filter_by(email=email).first()
        print(user)
        # Check if user is not existed.
        if user is None:

            return  {'message': "user not found "}, 404

        # if not user.is_active:
        #     return {'message': "user not active "}, 404

        # Generate an access token if the password is correct.
        # Three roles for user, default user role is user.
        # user：0，admin:1, sa:2
        print(user.verify_password(password))
        if user is not None and user.verify_password(password):

            if user.user_role == 'user':

                # Generate access token. This method takes boolean \
                # value for checking admin or normal user. Admin: 1 or 0.
                access_token = user.generate_auth_token(0)

            # If user is admin.
            elif user.user_role == 'admin':

                # Generate access token. This method takes boolean \
                # value for checking admin or normal user. Admin: 1 or 0.
                access_token = user.generate_auth_token(1)

            # If user is super admin.
            elif user.user_role == 'sa':

                # Generate access token. This method takes boolean \
                # value for checking admin or normal user. Admin: 2, 1, 0.
                access_token = user.generate_auth_token(2)

            else:
                return {"message": "invalid input."}, 422

            # Generate refresh_token based on the user emamil.
            refresh_token = (refresh_jwt.dumps({'email': email})).decode('ascii')

            # Commit session.
            db.session.commit()

            # raise error(status_code=200, return_code=1,message="fdsa")
            # raise notice(status_code=200, return_code=30000, action_status=True,playbook={
                    # 'user_id': user.id,
                    # 'is_active': user.is_active,
                    # 'username': user.username,
                    # 'user_role': user.user_role,
                    # 'access_token': access_token,
                    # 'refresh_token': refresh_token
                # })
            return {
                "message": "login success",
                "roles": [user.user_role],
                "access_token": "Bearer %s" % (access_token),
                "refresh_token": refresh_token,
                "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                "name": user.username
            }
            # return {
                #     'status':200,
                #     'message':"success",
                #     'user_id': user.id,
                #     'roles': 'editor',
                #     'is_active': user.is_active,
                #     'username': user.username,
                #     'user_role': user.user_role,
                #     'access_token': access_token,
                #     'refresh_token': refresh_token
                # }
        else:
            # Return invalid password
            raise notice(status_code=421,return_code=20003,action_status=False)


    @staticmethod
    def logout(data):
        # print (data)
        refresh_token = request.json.get('refresh_token')
        # print(refresh_token)

        # Get if the refresh token is in blacklist
        ref = Blacklist.query.filter_by(refresh_token=refresh_token).first()

        # Check refresh token is existed.
        if ref is not None:
            return {'status': 'already invalidated', 'refresh_token': refresh_token}

        # Create a blacklist refresh token.
        blacklist_refresh_token = Blacklist(refresh_token=refresh_token)

        # Add refresh token to db.
        save_changes(blacklist_refresh_token)

        # Return status of refresh token.
        return {'status': 'invalidated', 'refresh_token': refresh_token}

    @staticmethod
    def refresh_token(data):
        print (data)
        refresh_token = request.json.get('refresh_token')

        # Get if the refresh token is in blacklist
        ref = Blacklist.query.filter_by(refresh_token=refresh_token).first()
        print (ref)

        try:
            data = (refresh_jwt.loads(refresh_token))
            print (data)
            #print (s)

        except Exception as why:
            # Log the error.
            print (why)

        ## Create user not to add db. For generating token.
        user = User(email=data['email'])

        token = user.generate_auth_token(False)
        return {'access_token': token}
      