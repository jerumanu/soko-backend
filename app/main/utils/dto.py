from flask_restx import Namespace, fields

class CommentsDto:

    api = Namespace('comments', description='comments related operations')
    comments= api.model('comments', { 
        'created_on': fields.DateTime(required=True, description='user email address'),
        'comment': fields.String(required=True, description='user username'),
        'comment_owner': fields.String(description='user Identifier'),
        'update_at':fields.DateTime( required=True, description=' time the product was updated  '),
        'product_id':fields.Integer( required=True, description=' time the product was updated  ')


    })  


class ProductDto:
    
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'date_added': fields.DateTime( required=True, description=' time the product was created  '),
        'name': fields.String(required=True, description='product email address'),
        'description': fields.String(required=True, description='product productname'),
        'price': fields.Float(0.00,required=True, description='product price'),
        "image":fields.String(description='product Identifier'),
        'product_owner': fields.String(description='product Identifier'),
        'update_at':fields.DateTime( required=True, description=' time the product was updated '),
        # 'products':fields.List(
        # fields.String(attribute='comments', required=False),
        # description='array of tokens for all user devices',
        # attribute='comments')

})
    

class TimeDto():
    
    api = Namespace('timings', description='comments related operations')

    timings = api.model('timings', {
        'start_time': fields.DateTime(readonly=True, description='Time in HH:MM' ),
        'end_time': fields.DateTime(readonly=True, description='Time in HH:MM'),
        'closed_all_day': fields.Boolean(readOnly=True, description='True or False', default=False)
    })

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

