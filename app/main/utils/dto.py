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
        'id'          : fields.Integer(readonly= True, description="unique identifier"),
        'date_added'  : fields.DateTime( required=True, description=' time the product was created  '),
        'name'         : fields.String(required=True, description='product email address'),
        'description'  : fields.String(required=True, description='product productname'),
        'price'        : fields.Float(0.00,required=True, description='product price'),
        "image"        : fields.String(description='product Identifier'),
        'product_owner': fields.String(description='product Identifier'),
        'category'     : fields.String(description='category Identifier')
    })


class SubscribeDto:
    api = Namespace('Subscribe', description="Newsletter subscription")
    subscribe = api.model('Subscribe',{
        'id'       : fields.Integer(readonly= True, description="  unique identifier"),
        'email'    : fields.String(required=True, description="Email")
    })

class CategoryDto:
    api = Namespace('Category', description="Product category")
    category = api.model('Category',{
        'id'       : fields.Integer(readonly= True, description=" unique identifier."),
        'name'     : fields.String(required=True, description="Category name")
    })

class FaqDto:
    api = Namespace('Faq', description="FAQ")
    category = api.model('Faq',{
        'id'              : fields.Integer(readonly= True, description=" unique identifier"),
        'title'           : fields.String(required=True, description="FAQ title"),
        'description'     : fields.String(required=True, description="FAQ Description")
    })

class BlogDto:
    api = Namespace('Blog', description="Blog")
    blog = api.model('Blog',{
        'id'              : fields.Integer(readonly=True,  description=" unique identifier"),
        'title'           : fields.String(required=True,   description="Blog title"),
        'text'            : fields.String(required=True,   description="Subtitle"),
        'description'     : fields.String(required=True,   description="FAQ Description")
    })





class FavouriteDto:
    api = Namespace('favourite', description="favourite")
    favourite = api.model('Favourite',{
        'id'              : fields.Integer(readonly= True, description="unique identifier"),
        #'user_id'        : fields.Integer(required=True, description="user Id")
        'product_id'      : fields.Integer(required=True, description="product Id"),

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
        'firstname': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
class StarDto:
    api = Namespace('star', description='user related operations')
    star = api.model('star', {
        'rating':fields.Integer(description='user Identifier'),
        # 'four_stars': fields.Integer( description='user stars'),
        # 'three_stars':fields.Integer(description='user Identifier'),
        # 'two_stars':fields.Integer(description='user Identifier'),
        # 'one_star':fields.Integer(description='user Identifier')
    })

