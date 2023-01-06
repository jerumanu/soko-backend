from app.main import db
from app.main.qoutation.models.dereted_power import DeretedPanel
from app.main.qoutation.models.load_analysis import LoadAnalysis
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema             import DeretedSchema,LoadsSchema
from ..utils.dto                  import DeretedDto
from app.main.auth.extensions.auth import  role_required
from app.main.auth.extensions.auth.jwt_auth  import  auth
from app.main.auth.extensions.auth.api_doc_required import permission





api = DeretedDto.api
_dereted = DeretedDto.dereted

ITEM_NOT_FOUND = "Dereted panel power not found  not found."

dereted_schema= DeretedSchema()
loads_schema= LoadsSchema()
loads_list_schema =  LoadsSchema( many=True)

dereted_list_schema=  DeretedSchema(many=True)



@api.route('/<name>')
@api.param('name', 'The User identifier')
class ProductFilter(Resource):
    @permission
    @api.doc('get a product')
    @api.marshal_with(_dereted)
    def get(self, name):
        my_dict = dict()
        deretedpower_data = DeretedPanel.find_by_name(name)
        if deretedpower_data:
            result= dereted_schema.dump(deretedpower_data)

            # res = [test_list[0], test_list[-1]]

            

            




            
        



@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):

    @api.doc('delete  a product')
    @api.marshal_with(_dereted)

    def delete(self,id):
        deretedpower_data =  DeretedPanel.find_by_id(id)
        if deretedpower_data:
            deretedpower_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = DeretedPanel.find_by_id(id)
        if store_data:
            return dereted_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        


    @api.doc('delete a product')
    @api.marshal_with(_dereted)
    @api.expect(_dereted, validate=True)
    @auth.login_required
    @role_required.permission(2)
    def put(self, id):
        deretedpower_data =  DeretedPanel.find_by_id(id)
        dereted_json= request.get_json();

        if deretedpower_data:
            
            deretedpower_data.wp = dereted_json['wp']
            deretedpower_data.tstc= dereted_json['tstc']
            deretedpower_data.vmp = dereted_json['vmp']
            deretedpower_data.voc = dereted_json['voc']
            deretedpower_data.isc = dereted_json['isc']
            deretedpower_data.tcoeff = dereted_json['tcoeff']
            deretedpower_data.fman = dereted_json['fman']
            deretedpower_data.vcoeff = dereted_json['vcoeff']
            deretedpower_data.dirt = dereted_json['dirt']

        else:
            deretedpower_data = dereted_schema.load(dereted_json)

        deretedpower_data.save_to_db()

        return dereted_schema.dump(deretedpower_data), 200

@api.route('/')
class ProductList(Resource):

    @api.doc('list_of_dereted')
    @api.marshal_list_with(_dereted, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return dereted_list_schema.dump( DeretedPanel.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_dereted, validate=True)

    def post(self):

        dereted_json= request.get_json();
        

        print('wp',dereted_json['wp'])

        print("relusts",dereted_json)
        name = dereted_json['name']
        wp= dereted_json['wp'] 
        vmp= dereted_json['vmp']
        voc=dereted_json['voc']
        isc=dereted_json['isc']
        fman=dereted_json['fman']
        tstc=dereted_json['tstc']
        vcoeff=dereted_json['vcoeff']
        tcoeff= dereted_json ['tcoeff']
        dirt= dereted_json['dirt']
        print('name',name)

            # dirt=results['dirt']

            # tceff= -0.5
        
        
            # panelsvolts=12
            # num=0.2
            # s_factor=0.5
        print(wp)
        print(vmp)
        print(voc)
        print(isc)
        print(fman)
        print(tstc)
        print(vcoeff)

        # tceff = tamb + tstc
            
    

       
        print('dereted_json',dereted_json)
        deretedpower_data = dereted_schema.load(dereted_json)

        deretedpower_data.save_to_db()

        return dereted_schema.dump(deretedpower_data), 201