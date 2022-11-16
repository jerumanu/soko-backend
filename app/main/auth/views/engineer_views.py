from app.main import db

from app.main.auth.models.engineer_profile import Engineer
from flask                        import request
from flask_restx                  import Resource
from ..schema.schema             import EngineerSchema
from app.main.auth.utils.profile_dto                  import EngineerDto
from app.main.auth.extensions.auth import  role_required
from app.main.auth.extensions.auth.jwt_auth import  auth





api = EngineerDto.api
_engineer= EngineerDto.engineer

ITEM_NOT_FOUND = "Dereted panel power not found  not found."

engineer_schema= EngineerSchema()


engineer_list_schema= EngineerSchema(many=True)



   




            
        



@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):

    @api.doc('delete  a product')
    @api.marshal_with(_engineer)

    def delete(self,id):
        engineer_data =  Engineer.find_by_id(id)
        if engineer_data:
            engineer_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = Engineer.find_by_id(id)
        if store_data:
            return engineer_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        


    @api.doc('delete a product')
    @api.marshal_with(_engineer)
    @api.expect(_engineer, validate=True)
    @auth.login_required
    @role_required.permission(2)
    def put(self, id):
        engineer_data =  Engineer.find_by_id(id)
        engineer_json= request.get_json();

        if engineer_data:
            
            engineer_data.price = engineer_json['price']
            engineer_data.name = engineer_json['name']
            engineer_data.description = engineer_json['description']
            engineer_data.price  = engineer_json['price ']
            engineer_data.image = engineer_json['image']
            engineer_data.update_at = engineer_json['update_at']

        else:
            engineer_data = engineer_schema.load(engineer_json)

        engineer_data.save_to_db()
        return engineer_schema.dump(engineer_data), 200

@api.route('/')
class ProductList(Resource):

    @api.doc('list_of_engineer')
    @api.marshal_list_with(_engineer, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return engineer_list_schema.dump( Engineer.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_engineer, validate=True)

    def post(self):
        engineer_json= request.get_json()
        engineer_data = engineer_schema.load(engineer_json)
        
        engineer_data.save_to_db()

        return engineer_schema.dump(engineer_data), 201