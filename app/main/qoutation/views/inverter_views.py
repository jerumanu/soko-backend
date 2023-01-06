from app.main import db
from app.main.qoutation.models.inverter import Inverter
from app.main.qoutation.models.dereted_power import DeretedPanel
# from app.main.qoutation.models.load_analysis import LoadAnalysis
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema             import InverterSchema,DeretedSchema
from ..utils.dto                  import InverterDto
from app.main.auth.extensions.auth.api_doc_required import permission




api = InverterDto.api
_inverter  = InverterDto.inverter

ITEM_NOT_FOUND = "Dereted panel power not found  not found."


dereted_schema= DeretedSchema()
dereted_list_schema=  DeretedSchema(many=True)
inverter_Schema= InverterSchema()
inverter_list_Schema =  InverterSchema( many=True)



@api.route('/')
class ProductList(Resource):
    @permission
    @api.doc('list_of_inverter ')
    @api.marshal_list_with(_inverter , envelope='data')
    def get(self):
        return inverter_list_Schema.dump(Inverter.find_all()), 200


    @permission
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_inverter , validate=True)
    def post(self):
        inverter_json= request.get_json()
        name = inverter_json['name_panel']
        vmax= inverter_json['vmax']
        vmin = inverter_json['vmin']
        inveter_name = inverter_json['name']






        
        # ted_name= next(d for d in results if d['name'] == name)

        results1 =dereted_list_schema.dump( DeretedPanel.find_all())


        panel_name = next(d for d in results1 if d['name'] == name)

        print(panel_name)
        vmpold= panel_name['vmp']
        # vcoeff= panel_name['vcoeff']
        tstc= panel_name['tstc']
        vocold= panel_name['voc']
        vcoeff = 0.003
        print('helo',vcoeff)
        tamb = 30



        #  min no of panels in a string to be conected to inverter


        vmp_new   = vmpold +(-vcoeff*(tamb-tstc))
        print(vmp_new)
        
        

        min_panels= (vmin*1.1)/vmp_new
        print("min no of panels to inverter: ", min_panels)
        # max no of panes in a string tobe conected to inverter
        voc_new= vocold + (-vcoeff*(17-tstc))



        max_panels= (vmax*0.95)/voc_new


        data_json = dict()

        data_json['min_panels'] = min_panels
        data_json['max_panels'] = max_panels
        data_json['vmax'] = vmax
        data_json['vmin'] = vmin
        data_json['name'] = inveter_name
        

        print(data_json)


        print("max panels to inverter: ", max_panels)



        inverter_data= inverter_Schema.load(data_json)
        
        inverter_data.save_to_db()

        return inverter_Schema.dump(inverter_data), 201

