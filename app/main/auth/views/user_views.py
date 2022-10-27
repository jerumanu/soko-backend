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
    print (data['username'])
    # validate_email: 用于检测邮箱是否正确，并且真实可用
    if not validate_email(data['email'],verify=True,check_mx=True):
        
        # raise notice(status_code=500,return_code=20006,action_status=False)
        return {'message': "email not valid "}, 404
    
    if not data['password']  or  not data['username']:
        # raise notice(status_code=422,return_code=20007,action_status=False)
        return {'message': "email username not valid "}, 404
    if not user:
        user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            
        )
        save_changes(user) # 

        

        email_confirm_token =  (user.generate_confirmation_token(data['email'],data['username']))
        
        confirm_url = (url_for('api.confirm',confirm_token=email_confirm_token,_external=True)) + '?email=' + data['email']
        send_email(to=data['email'], subject='active',template='confirm.html', confirm_url=confirm_url,user=data['username'],)

        # send_email(to=data['email'], subject='active',template='email_tpl/confirm.html', confirm_url=confirm_url,user=data['username'],)

        # raise notice(playbook={
        #             'username': data['username'],
        #             'create_time': str(user.member_since),
        #             'confirm_url': str(confirm_url),
        # })

       

        # send confirm email to register user.
        # send_email(to=data['email'], subject='active',template='email_tpl/confirm', confirm_url=confirm_url,user=data['username'],)

        # confirm_url = (url_for('api.confirm',confirm_token=email_confirm_token,_external=True)) + '?email=' + data['email']

        # send confirm email to register user.
        # send_email(to=data['email'], subject='active',template='email_tpl/confirm', confirm_url=confirm_url,user=data['username'],)

    else:
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    # else:
    #     response_object = {
    #         'status': 'fail',
    #         'message': 'User already exists. Please Log in.',
    #     }
    #     return response_object, 409

        # Hash new user password
        # user.password(data['password'])

        # save_changes(user)

        # email_confirm_token =  (user.generate_confirmation_token(data['email'],data['username']))

        # confirm_url = (url_for('api.confirm',confirm_token=email_confirm_token,_external=True)) + '?email=' + data['email']

        # send confirm email to register user.
        # send_email(to=data['email'], subject='active',template='email_tpl/confirm', confirm_url=confirm_url,user=data['username'],)

        # raise notice(status_code=200,return_code=30001,action_status=True,playbook={
        #             'username': data['username'],
        #             'create_time': str(user.member_since),
        #             'confirm_url': str(confirm_url),
        # })
    # else:
    #     return {"message": "Does not exists." }, 409
       

def get_all_users():
    return User.query.all()



def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()
    


def save_changes(data):
    db.session.add(data)
    db.session.commit()



