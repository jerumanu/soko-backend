from app.main import db
from app.main.qoutation.models.batt import Batt
# from app.main.qoutation.models.load_analysis import LoadAnalysis
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema             import BattSchema
from ..utils.dto                  import BattDto
from app.main.auth.extensions.auth.api_doc_required import permission




api = BattDto.api
_dereted = BattDto.batt

ITEM_NOT_FOUND = "Dereted panel power not found  not found."


batt_Schema= BattSchema()
batt_list_Schema =  BattSchema( many=True)









@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):
    @permission
    @api.doc('delete  a product')
    @api.marshal_with(_dereted)
    def delete(self,id):
        batt_data= Batt.find_by_id(id)
        if batt_data:
            batt_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    @permission
    def get(self, id):
        store_data =Batt.find_by_id(id)
        if store_data:
            return batt_Schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        

    @permission
    @api.doc('delete a product')
    @api.marshal_with(_dereted)
    @api.expect(_dereted, validate=True)
    def put(self, id):
        batt_data= Batt.find_by_id(id)
        batt_json= request.get_json();

        if batt_data:
            
            batt_data.battv= batt_json['battv']
            batt_data.dod = batt_json['dod']
            batt_data.ah = batt_json['ah']
            batt_data.losses  = batt_json['losses']
            batt_data.nreff = batt_json['nreff']
            # batt_data.update_at = batt_json['update_at']

        else:
            batt_data= batt_Schema.load(batt_json)

        batt_data.save_to_db()
        return batt_Schema.dump(batt_data), 200

@api.route('/')
class ProductList(Resource):
    @permission
    @api.doc('list_of_dereted')
    @api.marshal_list_with(_dereted, envelope='data')
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return batt_list_Schema.dump(Batt.find_all()), 200

    @permission
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_dereted, validate=True)
    def post(self):
        batt_json= request.get_json()
        batt_data= batt_Schema.load(batt_json)
        
        batt_data.save_to_db()

        return batt_Schema.dump(batt_data), 201