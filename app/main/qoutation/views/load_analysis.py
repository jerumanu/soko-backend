from app.main import db
from app.main.qoutation.models.load_analysis import LoadAnalysis
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema              import LoadsSchema
from ..utils.dto                  import LoadsDto




api = LoadsDto.api
_loads = LoadsDto.loads

LOADS_NOT_FOUND = "Item not found."

loads_schema= LoadsSchema()

loads_list_schema =  LoadsSchema( many=True)




@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):

    @api.doc('delete  a product')
    @api.marshal_with( _loads)

    def delete(self,id):
        loads_analysis_data =  LoadAnalysis.find_by_id(id)
        if loads_analysis_data:
            loads_analysis_data.delete_from_db()
            return {'message': "Item Deleted successfully"}, 200
        return {'message': LOADS_NOT_FOUND}, 404

    def get(self, id):
        store_data = LoadAnalysis.find_by_id(id)
        if store_data:
            return  loads_schema.dump(store_data)
        return {'message': LOADS_NOT_FOUND}, 404    


    @api.doc('edit a load analysis')
    @api.marshal_with( _loads)
    @api.expect( _loads, validate=True)

    def put(self, id):
        loads_analysis_data =  LoadAnalysis.find_by_id(id)
        product_json= request.get_json();

        if loads_analysis_data:
            
            loads_analysis_data.price = product_json['price']
            loads_analysis_data.name = product_json['name']
            loads_analysis_data.description = product_json['description']
            loads_analysis_data.price  = product_json['price ']
            loads_analysis_data.image = product_json['image']
            loads_analysis_data.update_at = product_json['update_at']

        else:
            loads_analysis_data =  loads_schema.load(product_json)

        loads_analysis_data.save_to_db()
        return  loads_schema.dump(loads_analysis_data), 200


@api.route('/')
class ProductList(Resource):

    @api.doc('list_of _loads')
    @api.marshal_list_with( _loads, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return loads_list_schema.dump( LoadAnalysis.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect( _loads, validate=True)

    def post(self):
        product_json = request.get_json()
        loads_analysis_data =  loads_schema.load(product_json)
        
        loads_analysis_data.save_to_db()

        return loads_schema.dump(loads_analysis_data), 201
        

        # ted=results['tenegerydemand']
        # autonomy =results['autonomy ']
        # location=results['location']
        # latitude=results['latitude']
        # longtitude=results['longtitude']
        # systemvolts=results['systemvolts']

    
        



