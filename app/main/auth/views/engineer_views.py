
from app.main import db
from app.main.auth.models.engineer_profile import Engineer
from flask                        import request
from flask_restx                  import Resource
from ..schema.schema             import EngineerSchema
from app.main.auth.utils.profile_dto                  import EngineerDto
from app.main.auth.extensions.auth import  role_required
from app.main.auth.extensions.auth.jwt_auth import  auth
from app.main.auth.models.user import User
from app.main.decorators import subscription
from app.main.auth.extensions.auth.api_doc_required import permission



api = EngineerDto.api
_engineer= EngineerDto.engineer
ITEM_NOT_FOUND = "Dereted panel power not found  not found."
engineer_schema= EngineerSchema()
engineer_list_schema= EngineerSchema(many=True)



@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Engineers(Resource):
    @permission
    @api.doc('delete  a engineer')
    @api.marshal_with(_engineer)
    def delete(self,id):
        engineer_data =  Engineer.find_by_id(id)
        if engineer_data:
            engineer_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    @permission
    def get(self, id):
        store_data = Engineer.find_by_id(id)
        if store_data:
            return engineer_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        

    @permission
    @api.doc('delete a product')
    @api.marshal_with(_engineer)
    @api.expect(_engineer, validate=True)
    @subscription("engineer")
    def put(self, id):
        engineer_data = Engineer.query.filter_by(id=id).first_or_404(description=f"Engineer not found in database.")
        engineer_json = request.get_json();
        author        = User.query.filter_by(id=engineer_json['engineerUser']).first()
       
        if engineer_data:
            engineer_data.profesion     = engineer_json['profesion']
            engineer_data.engineerUser  = engineer_json['engineerUser']
            engineer_data.specification = engineer_json['specification']
            engineer_data.phoneNumber   = engineer_json['phoneNumber']
            engineer_data.location      = engineer_json['location']
            engineer_data.website       = engineer_json['website']
            engineer_data.linkdin       = engineer_json['linkdin']
            engineer_data.twitter       = engineer_json['twitter']
            engineer_data.instagram     = engineer_json['instagram']

        else:
            engineer_data = engineer_schema.load(engineer_json)

        if author:
            engineer_data.save_to_db()
            return engineer_schema.dump(engineer_data), 200
        else:
            return {"message": "Invalid User"}, 404


@api.route('/')
class EngineerList(Resource):
    @permission
    @api.doc('list_of_engineer')
    @api.marshal_list_with(_engineer, envelope='data')
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        return engineer_list_schema.dump(Engineer.find_all()), 200

    @permission
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_engineer, validate=True)
    @subscription("engineer")
    def post(self):
        engineer_json= request.get_json()
        engineerUser = User.query.filter_by(id=engineer_json['engineerUser']).first()
        if engineerUser:
            engineer_data = engineer_schema.load(engineer_json)
            engineer_data.save_to_db()
            return engineer_schema.dump(engineer_data), 201
        else:
            return{"message": "Invalid UserId"}