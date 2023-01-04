from flask_restx import Namespace, fields

class CommentsDto:

    api = Namespace('comments', description='comments related operations')
    comments= api.model('comments', {
        'comment': fields.String(required=True, description='comment'),
        'comment_owner': fields.Integer(required=True,  description="comment author"),
        'product_id':fields.Integer( required=True, description=' time the product was updated')
    })  


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'id'          : fields.Integer(readonly= True, description="unique identifier"),
        'name'        : fields.String(required=True, description='product email address'),
        'description' : fields.String(required=True, description='product productname'),
        'price'       : fields.Float(0.00,required=True, description='product price'),
        "image"       : fields.String(description='product Identifier'),
        'inStock'     : fields.Boolean(required=True, description="is the product available"),
        'condition'   : fields.String(required=True, description="Is the product new or used"),
        'solarType_id': fields.Integer(required=True, description="Solar type Id"),
        'brand_id'    : fields.Integer(required=True, description="Brand Id"),
        'category_id'    : fields.Integer(required=True, description='category Identifier'),         
        'product_owner': fields.Integer(required=True,  description="Author id")

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

        'id'       : fields.Integer(readonly= True, description="unique identifier"),
        'name'     : fields.String(required=True, description="Category name"),
        'author'   : fields.Integer(required=True, description="User Id")
    
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
        'description'     : fields.String(required=True,   description="Blog Description"),
        'author'          : fields.Integer(required=True,  description="Author id")
    })





class FavouriteDto:
    api = Namespace('favourite', description="favourite")
    favourite = api.model('Favourite',{
        'id'              : fields.Integer(readonly= True, description="unique identifier"),
        'user_id'        : fields.Integer(required=True, description="user Id"),
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
        'email'    : fields.String(required=True, description='user email address'),
        'password' : fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
class StarDto:
    api = Namespace('star', description='user related operations')
    star = api.model('star', {
        'rating':fields.Integer(description='user Identifier'),
        'rate':fields.Integer(description='rating Identifier'),
        # 'four_stars': fields.Integer( description='user stars'),
        # 'three_stars':fields.Integer(description='user Identifier'),
        # 'two_stars':fields.Integer(description='user Identifier'),
        # 'one_star':fields.Integer(description='user Identifier')
    })



class InvoiceDto:
    api     = Namespace('invoice payment', description='payment for services provided')
    payment = api.model('invoice', {
        'amount'      : fields.Float(required=True,  description='amount'),
        'phoneNumber' : fields.String(required=True, description='number to pay'),
        'user_id'     : fields.Integer(required=True, description='user id'),
        'paymentType' : fields.String(required = True, description='Payment type')
    })

class TransactionDto:
    api     = Namespace('Transaction payment', description='payment for services provided')
    transaction = api.model('transaction', {
        'receipt_id '        : fields.String(required=True, description='payment reciept'),
        'date_paid '         : fields.String(required=True, description='date paid'),
        'merchant_request_id': fields.String(required=True, description='merchant id'),
        'amount'             : fields.Float (required=True, description='amount'),
        'phoneNumber'        : fields.String(required=True, description='phone number'),
        'user_id'            : fields.String(required=True, description='user id'),
        'paymentType'        : fields.String(required=True, description='Payment type')
    })


class BrandDto:
    api     = Namespace('Brand name', description='Product brand name')
    brand   = api.model('brand', {
        'id'    : fields.Integer(readonly=True,  description="unique identifier"),
        'name'  : fields.String(required=True,   description="Product Brand name"),
        'author': fields.Integer(required=True,  description="Author id")
    })


class SolarTypeDto:
    api       = Namespace('Solar type', description='Type of solar in the market')
    solarType = api.model('solarType', {
        'id'    : fields.Integer(readonly=True,  description="unique identifier"),
        'name'  : fields.String(required=True,   description="solar type name"),
        'author': fields.Integer(required=True,  description="Author id")
    })

