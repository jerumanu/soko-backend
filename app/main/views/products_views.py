
from app.main import db
from app.main.model.product_model import ProductModel


from flask import request
from flask_restx import Resource

from ..schema.schema import ProductSchema



from ..utils.dto import ProductDto



api = ProductDto.api
_products = ProductDto.product

ITEM_NOT_FOUND = "Item not found."

item_schema= ProductSchema()
item_list_schema =  ProductSchema( many=True)


@api.route('/<name>')
@api.param('name', 'The User identifier')
class ProductFilter(Resource):
    @api.doc('get a product')
    @api.marshal_with(_products)
    def get(self, name):
        item_data = ProductModel.find_by_name(name)
        if item_data:
            return item_schema.dump(item_data)
        return {'message': ITEM_NOT_FOUND}, 404
@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):     
    @api.doc('delete  a product')
    @api.marshal_with(_products)

    def delete(self,id):
        item_data =  ProductModel.find_by_id(id)
        if item_data:
            item_data.delete_from_db()
            return {'message': "Item Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = ProductModel.find_by_id(id)
        if store_data:
            return item_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404    


    @api.doc('delete a product')
    @api.marshal_with(_products)
    @api.expect(_products, validate=True)
    def put(self, id):
        item_data =  ProductModel.find_by_id(id)
        item_json = request.get_json();

        if item_data:
            item_data.price = item_json['price']
            item_data.name = item_json['name']
        else:
            item_data = item_schema.load(item_json)

        item_data.save_to_db()
        return item_schema.dump(item_data), 200

@api.route('/')
class ProductList(Resource):
    @api.doc('list_of_products')
    @api.marshal_list_with(_products, envelope='data')
    
    def get(self):
        return item_list_schema.dump( ProductModel.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_products, validate=True)
    def post(self):
        item_json = request.get_json()
        item_data = item_schema.load(item_json)
        item_data.save_to_db()

        return item_schema.dump(item_data), 201