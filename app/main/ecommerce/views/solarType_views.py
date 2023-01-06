from flask                     import request, jsonify
from flask_restx               import Resource
from app.main.ecommerce.model.submodel   import *
from app.main.ecommerce.schema.schema    import SolarTypeSchema
from app.main.ecommerce.utils.dto        import SolarTypeDto
from ....main                       import db
from app.main.auth.models.user      import User
from app.main.auth.extensions.auth.api_doc_required import permission




api              = SolarTypeDto.api
_solarType       = SolarTypeDto.solarType
item_schema      = SolarTypeSchema()
item_list_schema = SolarTypeSchema(many=True)



@api.route("/")
class SolarList(Resource):
    @permission
    @api.doc('List of solar type')
    @api.marshal_list_with(_solarType , envelope='data')
    def get(self):
        return item_list_schema.dump(SolarType.find_all()), 200

    @permission
    @api.response(201, 'Brand name added successfully')
    @api.doc("Adding solar type name")
    @api.expect(_solarType, validate=True)
    def post(self):
        item_json         = request.get_json()
        nameConfirmation  = SolarType.query.filter_by(name=item_json["name"]).first()
        author            = User.query.filter_by(id=item_json['author']).first()

        if author:

            if not nameConfirmation:
                item_data = item_schema.load(item_json)
                db.session.add(item_data)
                db.session.commit()
                return item_schema.dump(item_data), 201
                    
            else:
                return {"message": "Name already exist"}, 401
        else:
            return {"message": "Invalid user ID"}, 404


@api.route('/user/<int:userId>')
@api.param('UserId', 'The User identifier')
class Solar(Resource):
    @permission
    @api.doc('Your owner')
    @api.marshal_list_with(_solarType , envelope='data')
    def get(self, userId):
        solarType = SolarType.query.filter_by(author=userId).all()
        if solarType:
            return item_list_schema.dump(solarType), 201
        return jsonify({
            "message": "You haven't uploaded any Product yet"
        }), 401


@api.route('/<int:id>')
class Solar(Resource):
    @permission
    @api.doc('deleting solar type')
    @api.marshal_with(_solarType)
    def delete(self, id):
        item_data = SolarType.query.filter_by(id=id).first()
        if not item_data:
            return{"message":"Item is not found"}, 401
        else:
            db.session.delete(item_data)
            db.session.commit()
            return {"message":"deleted successfully"}, 201


    @permission
    @api.doc("get solar type by id")
    @api.marshal_with(_solarType)
    def get(self, id):
        item_data = SolarType.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        return item_schema.dump(item_data), 201

        
    @permission
    @api.doc('edit solar type name')
    @api.marshal_with(_solarType)
    @api.expect(_solarType, validate=True)
    def put(self, id):
        item_data = SolarType.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        item_json = request.get_json()

        if item_data:
            item_data.name=item_json['name']
            db.session.add(item_data)
            db.session.commit()
            return  item_schema.dump(item_data), 200
        



