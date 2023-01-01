from datetime                     import date, datetime, timedelta
from functools                    import wraps
from app.main.ecommerce.model.payment_model import Transaction


def subscription(paymentType, userId):
    def payment(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            payment_data = Transaction.query.filter_by(user_id=userId, paymentType=paymentType).first_or_404(description='No payment Found')
            startDate    = payment_data['startDate']
            day          = payment_data['day']
            daytoday     = date.today() 
            enddate      = startDate + timedelta(day)
            
            if(daytoday > enddate):
                return {
                "message": "The subscription has ended"
                }, 401
            return func(*args, **kwargs)
        return wrapper
    return payment