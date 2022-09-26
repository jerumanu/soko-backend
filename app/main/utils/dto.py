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