from datetime                     import date, datetime, timedelta
from functools                    import wraps
from app.main.ecommerce.model.payment_model import Transaction
from app.main.auth.extensions.auth.jwt_auth import jwt
from app.main.auth.models.user import User
from flask import request
from app.main.ecommerce.model.product_model import ProductModel


def subscription(paymentType):
    def payment(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = None
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            if not token:
                return {'message' : 'Token is missing !!k'}, 401
      
            data = jwt.loads(token)
            current_user = User.query.filter_by(email = data['email']).first()
            payment_data = Transaction.query.filter_by(user_id=current_user, paymentType=paymentType).first_or_404(description='No payment Found')
            startDate    = payment_data['startDate']
            day          = payment_data['day']
            daytoday     = date.today() 
            enddate      = startDate + timedelta(day)
            
            
            if(daytoday > enddate):
                return {
                "message": "The subscription has ended"
                }, 401
            
            product=ProductModel.query.filter(product_owner=current_user).count()
            if product == 3:
                return {
                    "message": "kindly make payments"
                }, 401
            return func(*args, **kwargs)
        return wrapper
    return payment