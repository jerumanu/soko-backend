from flask                     import request
from flask_restx               import Resource
from app.main.model.submodel   import *
from app.main.schema.schema    import SolarTypeSchema
from app.main.utils.dto        import SolarTypeDto
from ..                        import db




api              = SolarTypeDto.api
_solarType       = SolarTypeDto.solarType
item_schema      = SolarTypeSchema()
item_list_schema = SolarTypeSchema(many=True)



@api.route("/")
class BrandList(Resource):
    @api.doc('List of solar type')
    @api.marshal_list_with(_solarType , envelope='data')
    def get(self):
        return item_list_schema.dump(SolarType.find_all()), 200


    @api.response(201, 'Brand name added successfully')
    @api.doc("Adding solar type name")
    @api.expect(_solarType, validate=True)
    def post(self):
        item_json         = request.get_json()
        nameConfirmation  = SolarType.query.filter_by(name=item_json["name"]).first()

        if not nameConfirmation:
            item_data = item_schema.load(item_json)
            db.session.add(item_data)
            db.session.commit()
            return item_schema.dump(item_data), 201
                
        else:
            return {"message": "Name already exist"}, 201


@api.route('/<int:id>')
class Brand(Resource):
    @api.doc('deleting solar type')
    @api.marshal_with(_solarType)
    def delete(self, id):
        item_data = SolarType.query.filter_by(id=id).first()
        if not item_data:
            return{"message":"Item is not found"}
        else:
            db.session.delete(item_data)
            db.session.commit()
            return {"message":"deleted successfully"}

    
    @api.doc("get solar type by id")
    @api.marshal_with(_solarType)
    def get(self, id):
        item_data = SolarType.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        return item_schema.dump(item_data), 200

        

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



