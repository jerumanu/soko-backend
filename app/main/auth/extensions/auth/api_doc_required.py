# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: api_doc_required.py
# @Date:   2018-08-19 23:42:48
from flask import request
from functools import wraps 
from app.main.auth.extensions.auth.jwt_auth import jwt
from app.main.auth.models.user import User

def permission(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return {'message' : 'Token is missing !!k'}, 401
        try:
            data = jwt.loads(token)
            current_user = User.query.filter_by(email = data['email']).first()
            return  f(current_user, *args, **kwargs)
        except:
            return {
                'message' : 'Token is invalid t !!'
            }, 401
    return decorated