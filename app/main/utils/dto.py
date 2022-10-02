from flask_restx import Namespace, fields

class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'date_added': fields.DateTime( required=True, description=' time the product was created  '),
        'name': fields.String(required=True, description='product email address'),
        'description': fields.String(required=True, description='product productname'),
        'price': fields.Integer(required=True, description='product price'),
        "image":fields.String(description='product Identifier'),
        'product_owner': fields.String(description='product Identifier')
    })


class SubscribeDto:
    api = Namespace('Subscribe', description="Newsletter subscription")
    subscribe = api.model('Subscribe',{
        'id'       : fields.Integer(readonly= True, description="unique identifier"),
        'email'    : fields.String(required=True, description="Email")
    })

class CategoryDto:
    api = Namespace('Category', description="Product category")
    category = api.model('Category',{
        'id'       : fields.Integer(readonly= True, description="unique identifier"),
        'name'     : fields.String(required=True, description="Category name")
    })

class FaqDto:
    api = Namespace('Faq', description="FAQ")
    category = api.model('Faq',{
        'id'              : fields.Integer(readonly= True, description="unique identifier"),
        'title'           : fields.String(required=True, description="FAQ title"),
        'description'     : fields.String(required=True, description="FAQ Description")
    })

class BlogDto:
    api = Namespace('Blog', description="Blog")
    blog = api.model('Blog',{
        'id'              : fields.Integer(readonly=True, description="unique identifier"),
        'title'           : fields.String(required=True,   description="Blog title"),
        'text'            : fields.String(required=True,   description="Subtitle"),
        'description'     : fields.String(required=True,   description="FAQ Description")
    })