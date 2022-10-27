from app.main                     import db
from app.main import db
from app.main.model.product_model import ProductModel
from flask                        import request
from flask_restx                  import Resource
from ..schema.schema              import ProductSchema
from ..utils.dto                  import ProductDto




api = ProductDto.api
_products = ProductDto.product

ITEM_NOT_FOUND = "Item not found."

product_schema= ProductSchema()

product_list_schema =  ProductSchema( many=True)


@api.route('/<name>')
@api.param('name', 'The User identifier')
class ProductFilter(Resource):

    @api.doc('get a product')
    @api.marshal_with(_products)
    def get(self, name):
        item_data = ProductModel.find_by_name(name)
        if item_data:
            
            return {'message': ITEM_NOT_FOUND}, 404


        product_data = ProductModel.find_by_name(name)
        if product_data:
            return product_schema.dump(product_data)
        return {'message': ITEM_NOT_FOUND}, 404

@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):

    @api.doc('delete  a product')
    @api.marshal_with(_products)

    def delete(self,id):
        product_data =  ProductModel.find_by_id(id)
        if product_data:
            product_data.delete_from_db()
            return {'message': "Item Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = ProductModel.find_by_id(id)
        if store_data:
            return product_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404    


    @api.doc('delete a product')
    @api.marshal_with(_products)
    @api.expect(_products, validate=True)

    def put(self, id):
        product_data =  ProductModel.find_by_id(id)
        product_json = request.get_json();

        if product_data:
            
            product_data.price = product_json['price']
            product_data.name = product_json['name']
            product_data.description = product_json['description']
            product_data.price  = product_json['price ']
            product_data.image = product_json['image']
            product_data.update_at = product_json['update_at']

        else:
            product_data = product_schema.load(product_json)

        product_data.save_to_db()
        return product_schema.dump(product_data), 200

@api.route('/')
class ProductList(Resource):

    @api.doc('list_of_products')
    @api.marshal_list_with(_products, envelope='data')
    
    def get(self):
        
        
        return product_list_schema.dump( ProductModel.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_products, validate=True)

    def post(self):
        product_json = request.get_json()
        product_data = product_schema.load(product_json)
        product_data.save_to_db()

        return product_schema.dump(product_data), 201