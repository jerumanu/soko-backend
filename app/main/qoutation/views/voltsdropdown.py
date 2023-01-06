from app.main import db
from app.main.qoutation.models.voltdropdown  import VoltsDropDowm
from app.main.qoutation.models.dereted_power import DeretedPanel
# from app.main.qoutation.models.load_analysis import LoadAnalysis
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema             import VoltageDropSchema,DeretedSchema
from ..utils.dto                  import VoltsDropDto
from app.main.auth.extensions.auth.api_doc_required import permission




api = VoltsDropDto.api
_dropdown = VoltsDropDto.dropdown

ITEM_NOT_FOUND = "Dereted panel power not found  not found."


volts_Schema= VoltageDropSchema()
volts_list_Schema =  VoltageDropSchema( many=True)



dereted_schema= DeretedSchema()
dereted_list_schema=  DeretedSchema(many=True)





@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):
    @permission
    @api.doc('delete  a product')
    @api.marshal_with(_dropdown )
    def delete(self,id):
        voltsdrop_data= VoltsDropDowm.find_by_id(id)
        if voltsdrop_data:
            voltsdrop_data.delete_from_db()
            return {'message': "dereted panel power Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    @permission
    def get(self, id):
        store_data =VoltsDropDowm.find_by_id(id)
        if store_data:
            return volts_Schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

        


    

@api.route('/')
class ProductList(Resource):
    @permission
    @api.doc('list_of_dropdown ')
    @api.marshal_list_with(_dropdown , envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return volts_list_Schema.dump(VoltsDropDowm.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_dropdown , validate=True)
    @permission
    def post(self):
        volts_json= request.get_json()
        DROPDOWN = 0.02

        rho=volts_json['rho']
        length=volts_json['length']
        systemvolts=volts_json['systemvolts']
        name = volts_json['name_panel']
        cable= volts_json['cable']
        
        # ted_name= next(d for d in results if d['name'] == name)

        results1 =dereted_list_schema.dump( DeretedPanel.find_all())

        panel_name= next(d for d in results1 if d['name'] == name)

        isc = panel_name['isc']



        area= (2*isc * rho *length )/(DROPDOWN * systemvolts)

        voltage_json =dict()

        voltage_json['rho']=rho
        voltage_json['length']=length
        voltage_json['systemvolts']=systemvolts
        voltage_json['name_panel'] =name
        voltage_json['isc']=isc
        voltage_json['area']=area
        voltage_json['cable']=cable


        voltsdrop_data= volts_Schema.load(voltage_json)
        
        voltsdrop_data.save_to_db()

        return volts_Schema.dump(voltsdrop_data), 201