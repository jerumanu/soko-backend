from app.main import db
from app.main.qoutation.models.cablesize import CableDropDown
# from app.main.qoutation.models.load_analysis import LoadAnalysis
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema             import CableDropSchema
from ..utils.dto                  import CableDropDto





api =  CableDropDto.api
_cable =  CableDropDto.cable

ITEM_NOT_FOUND = "Dereted panel power not found  not found."


cable_Schema= CableDropSchema()
cable_list_Schema =  CableDropSchema( many=True)









@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):

    @api.doc('delete  a product')
    @api.marshal_with(_cable)

    def delete(self,id):
        cable_data= CableDropDown.find_by_id(id)
        if cable_data:
            cable_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data =CableDropDown.find_by_id(id)
        if store_data:
            return cable_Schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        


    @api.doc('delete a product')
    @api.marshal_with(_cable)
    @api.expect(_cable, validate=True)

    def put(self, id):
        cable_data= CableDropDown.find_by_id(id)
        cable_json= request.get_json();

        if cable_data:
            
            cable_data.cable = cable_json['cable']
            cable_data.rho = cable_json['rho']
            
            # cable_data.update_at = cable_json'update_at']

        else:
            cable_data= cable_Schema.load(cable_json)

        cable_data.save_to_db()
        return cable_Schema.dump(cable_data), 200

@api.route('/')
class ProductList(Resource):

    @api.doc('list_of_cable')
    @api.marshal_list_with(_cable, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return cable_list_Schema.dump(CableDropDown.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_cable, validate=True)

    def post(self):
        cable_json= request.get_json()
        cable_data= cable_Schema.load(cable_json)
        
        cable_data.save_to_db()

        return cable_Schema.dump(cable_data), 201