from app.main import db
from app.main.qoutation.models.dereted_power import DeretedPanel
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema             import DeretedSchema
from ..utils.dto                  import DeretedDto




api = DeretedDto.api
_products = DeretedDto.product

ITEM_NOT_FOUND = "Dereted panel power not found  not found."

product_schema= DeretedSchema()

product_list_schema =  DeretedSchema( many=True)


@api.route('/<name>')
@api.param('name', 'The User identifier')
class ProductFilter(Resource):

    @api.doc('get a product')
    @api.marshal_with(_products)
    def get(self, name):
        power_data= DeretedPanel.find_by_name(name)
        if power_data:
            
            return {'message': ITEM_NOT_FOUND}, 404


        deretedpower_data = DeretedPanel.find_by_name(name)
        if deretedpower_data:
            return product_schema.dump(deretedpower_data)
            
        return {'message': ITEM_NOT_FOUND}, 404

@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):

    @api.doc('delete  a product')
    @api.marshal_with(_products)

    def delete(self,id):
        deretedpower_data =  DeretedPanel.find_by_id(id)
        if deretedpower_data:
            deretedpower_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = DeretedPanel.find_by_id(id)
        if store_data:
            return product_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404    


    # @api.doc('delete a product')
    # @api.marshal_with(_products)
    # @api.expect(_products, validate=True)

    # def put(self, id):
    #     deretedpower_data =  DeretedPanel.find_by_id(id)
    #     product_json = request.get_json();

    #     if deretedpower_data:
            
    #         deretedpower_data.price = product_json['price']
    #         deretedpower_data.name = product_json['name']
    #         deretedpower_data.description = product_json['description']
    #         deretedpower_data.price  = product_json['price ']
    #         deretedpower_data.image = product_json['image']
    #         deretedpower_data.update_at = product_json['update_at']

    #     else:
    #         deretedpower_data = product_schema.load(product_json)

    #     deretedpower_data.save_to_db()
    #     return product_schema.dump(deretedpower_data), 200

@api.route('/')
class ProductList(Resource):

    @api.doc('list_of_products')
    @api.marshal_list_with(_products, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return product_list_schema.dump( DeretedPanel.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_products, validate=True)

    def post(self):
        product_json = request.get_json()
        deretedpower_data = product_schema.load(product_json)
        
        deretedpower_data.save_to_db()

        return product_schema.dump(deretedpower_data), 201