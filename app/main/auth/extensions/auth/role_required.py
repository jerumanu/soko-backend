import functools
from flask import request
from app.main.auth.extensions.auth.jwt_auth import jwt
from app.main.auth.models.user import User

def permission(arg ):
    def check_permissions(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            token = None
            print("token 1", token)
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            print("token 2", token)
            if not token:
                return {'message' : 'Token is missing !!k'}, 401
            data = jwt.loads(token)
            print("data 1", data)
            try:
                data = jwt.loads(token)
                print("data", data)
                current_user = User.query.filter_by(email = data['email']).first()
                print("the current user id", current_user.id)

                # Just print info
                if data['admin'] == 4  :
                    print ("Your role is sa .")
                elif data['admin']== 3  :
                    print('your role is businees owner')
                elif data['admin']==2 :
                    print('your role is engineer')

                elif data['admin'] == 1:
                    print ("Your role is admin .")
                else:
                    print ("Your role is user .")

                # Determine permissions based on permission_level
                if data['admin'] < arg:
                    # If user role does't right , return info
                    return {"message": "Permission denied, your role code is {} .".format(data['admin'])}, 403

            except ValueError:
                # The Authorization header is either empty or has no token.
                return {"message": "Headr Not Found ."}, 404

            except Exception :
                # logging.error(why)

                # If it does not generated return false.
                return {"message": "Invalid input ."}, 422

                    # Return method.
            return  f(current_user, *args, **kwargs)

        # Return decorated method.
        return decorated
    # Return check permissions method.
    return check_permissions




