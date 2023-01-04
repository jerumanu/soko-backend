from app.main import db
from app.main.auth.models.business_profile import Business
from app.main.auth.models.user import User
from flask                        import request
from flask_restx                  import Resource
from ..schema.schema             import BusinessSchema
from app.main.auth.utils.profile_dto             import BusinessDto 

from app.main.auth.extensions.auth import  role_required
from app.main.auth.extensions.auth.jwt_auth import  auth
from flask_login import login_required






api = BusinessDto.api
_business = BusinessDto.business
ITEM_NOT_FOUND = "business  not found  not found."
business_schema= BusinessSchema()
business_list_schema=  BusinessSchema(many=True)



@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Businesses(Resource):

    @api.doc('delete  a business')
    @api.marshal_with(_business)

    def delete(self,id):
        business_data =  Business.find_by_id(id)
        if business_data:
            business_data.delete_from_db()
            return {'message': "business  Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = Business.find_by_id(id)
        if store_data:
            return business_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        


    @api.doc('edit a business')
    @api.marshal_with(_business)
    @api.expect(_business, validate=True)
    # @auth.login_required
    # @role_required.permission(2)
    def put(self, id):
        business_data = Business.query.filter_by(id=id).first_or_404(description=f"Business not found in database.")
        business_json= request.get_json()
        business_owner= User.query.filter_by(id=business_json['business_owner']).first()



        if business_data:
            business_data.business_name     = business_json['business_name']
            business_data.business_owner    = business_json['business_owner']
            business_data.business_desc     = business_json['business_desc']
            business_data.specific_location = business_json['specific_location']
            business_data.to_hour           = business_json['to_hour']
            business_data.weekday           = business_json['weekday']
            business_data.from_hour         = business_json['from_hour']

        else:
            business_data = business_schema.load(business_json)

        if business_owner:
            business_data.save_to_db()
            return business_schema.dump(business_data), 200
        else:
            return {"message": "Invalid User"}, 404

@api.route('/')
class businessList(Resource):

    @api.doc('list_of_business')
    @api.marshal_list_with(_business, envelope='data')
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return business_list_schema.dump( Business.find_all()), 200

    @api.response(201, 'business successfully created.')
    @api.doc('create a new Product')
    @api.expect(_business, validate=True)
    # @login_required
    # @role_required.permission(3)
    def post(self):
        business_json= request.get_json()
        businessOwner = User.query.filter_by(id=business_json['business_owner']).first()
        if businessOwner:
            business = business_schema.load(business_json)
            business.save_to_db()
            return business_schema.dump(business), 201
        else:
            return{"message": "Invalid UserId"},404