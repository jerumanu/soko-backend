import datetime
import uuid
from flask import url_for
from ....main import db
from app.main.auth.models.user import User
from validate_email_address import validate_email
from app.main.auth.mails.email  import send_email
from     app.errors  import CustomFlaskErr as notice



def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    # print (data['username'])
   
    if not validate_email(data['email'],verify=True,check_mx=True):
        
        # raise notice(status_code=500,return_code=20006,action_status=False)
        return {'message': "email not valid "}, 404
    
    if not data['password']  or  not data['firstname']:
        # raise notice(status_code=422,return_code=20007,action_status=False)
        return {'message': "email firstname not valid "}, 404
    if not user:
        user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            password=data['password'],
            user_role=data['user_role']
        )
        save_changes(user) # 

        

       
        
    
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201


def get_all_users():
    return User.query.all()



def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()
    


def save_changes(data):
    db.session.add(data)
    db.session.commit()



