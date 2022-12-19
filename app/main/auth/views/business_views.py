from app.main import db
from app.main.auth.models.business_profile import Business


from flask                        import request
from flask_restx                  import Resource
from ..schema.schema             import BusinessSchema
from app.main.auth.utils.profile_dto             import BusinessDto 

from app.main.auth.extensions.auth import  role_required
from app.main.auth.extensions.auth.jwt_auth import  auth
from flask_login import login_required






api = BusinessDto.api
_business = BusinessDto.business
ITEM_NOT_FOUND = "Dereted panel power not found  not found."
business_schema= BusinessSchema()
business_list_schema=  BusinessSchema(many=True)



@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):

    @api.doc('delete  a product')
    @api.marshal_with(_business)

    def delete(self,id):
        deretedpower_data =  Business.find_by_id(id)
        if deretedpower_data:
            deretedpower_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = Business.find_by_id(id)
        if store_data:
            return business_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        


    @api.doc('delete a product')
    @api.marshal_with(_business)
    @api.expect(_business, validate=True)
    @auth.login_required
    @role_required.permission(2)
    def put(self, id):
        deretedpower_data =  Business.find_by_id(id)
        dereted_json= request.get_json();

        if deretedpower_data:
            
            deretedpower_data.price = dereted_json['price']
            deretedpower_data.name = dereted_json['name']
            deretedpower_data.description = dereted_json['description']
            deretedpower_data.price  = dereted_json['price ']
            deretedpower_data.image = dereted_json['image']
            deretedpower_data.update_at = dereted_json['update_at']

        else:
            deretedpower_data = business_schema.load(dereted_json)

        deretedpower_data.save_to_db()
        return business_schema.dump(deretedpower_data), 200

@api.route('/')
class ProductList(Resource):

    @api.doc('list_of_business')
    @api.marshal_list_with(_business, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return business_list_schema.dump( Business.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_business, validate=True)
    # @login_required
    @role_required.permission(3)
    def post(self):
        
        dereted_json= request.get_json()
        deretedpower_data = business_schema.load(dereted_json)
        
        deretedpower_data.save_to_db()

        return business_schema.dump(deretedpower_data), 201