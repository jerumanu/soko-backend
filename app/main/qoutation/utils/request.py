import requests
from app.main import db
from app.main.qoutation.models.dereted_power import DeretedPanel
from app.main.qoutation.models.load_analysis import LoadAnalysis
from app.main.qoutation.models.batt import Batt
from flask                        import request
from flask_restx                  import Resource
from ..schemas.schema             import DeretedSchema,LoadsSchema,BattSchema
from ..utils.dto                  import DeretedDto





api = DeretedDto.api
_dereted = DeretedDto.dereted

ITEM_NOT_FOUND = "Dereted panel power not found  not found."

dereted_schema= DeretedSchema()
dereted_list_schema=  DeretedSchema(many=True)

loads_schema= LoadsSchema()
loads_list_schema =  LoadsSchema( many=True)

batt_Schema= BattSchema()
batt_list_Schema =  BattSchema( many=True)




@api.route('/<name>')
@api.param('name', 'The User identifier')
class ProductFilter(Resource):
   
    @api.doc('get a product')
    @api.marshal_with(_dereted)


    def get(self, name):

        my_dict=dict()
        deretedpower_data = DeretedPanel.find_by_name(name)
        if deretedpower_data:
            result= dereted_schema.dump(deretedpower_data)
            # res = [test_list[0], test_list[-1]]
            print("relusts",result)
            wp= result['wp'] 
            vmp= result['vmp']
            voc=result['voc']
            isc=result['isc']
            fman=result['fman']
            tstc=result['tstc']
            vcoeff=result['vcoeff']
            # dirt=results['dirt']
            tceff= -0.5
            tamb= 20
            dirt=0.98
            panelsvolts=12
            num=0.2
            s_factor=0.5
            print(wp)
            print(vmp)
            print(voc)
            print(isc)
            print(fman)
            print(tstc)
            print(vcoeff)

            wpd = round(wp * (1 + ((tceff/100) * (tamb - tstc))) * (1-dirt) * (1-fman))
            # self.wpd
            # panels = round(power /wpd)
            # my_cal['wpd']=wpd
            print("wpd",wpd)
            my_dict['wpd']=wpd

            
       
        

        # return results

        
# def panels(self):

#     panels = round(power /wpd)


        payload={'lat':40,'lon':-105}

        payload['lat']=30

        payload['lon']=80

        #print(r['inputs']['log'])
        print (payload)
        r=requests.get('https://developer.nrel.gov/api/pvwatts/v6.json?api_key=DEMO_KEY&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10', params=payload).json()


        print('latitude of the area',
          r['inputs']['lat']
          
        )

        print(r['inputs']['log'])
        print('annual psh of the area',r['outputs']["solrad_annual"])
        print("psh of the area",r['outputs']["solrad_monthly"])
        PSH=min(r["outputs"]["solrad_monthly"])

        results=loads_list_schema.dump( LoadAnalysis.find_all())
        

        print('results1',results)
        my_dict['PSH']=PSH
        TED=results['tenegerydemand']
        autonomy =results['autonomy ']
        location=results['location']
        latitude=results['latitude']
        longtitude=results['longtitude']
        systemvolts=results['systemvolts']

        print(TED)
        print(autonomy)
        print(location)
        print(latitude)
        print(longtitude)
        print(systemvolts)


        power = TED / PSH

        print (power)

        panels = round(power /wpd)

        print(panels)

        panels_parallel = round(((panels * panelsvolts) / systemvolts) + num)

        series = systemvolts / panelsvolts
        print("no of panel in series: ", series)

        #total panels required
        totalpanels = series * panels_parallel
        print("Final total number of panels: ", totalpanels)

        

        #charge controller
        charge_controller = s_factor * isc * panels_parallel
        print("charge of controller: ", charge_controller)

        my_dict['power']=power
        my_dict['panels']=panels
        my_dict['series']=series
        my_dict['panels_parallel']=panels_parallel
        my_dict['totalpanels']=totalpanels
        my_dict['charge_controler']=charge_controller


        batt_results =batt_list_Schema.dump(Batt.find_all()), 200

        battvolts = batt_results['battv']
        dod =batt_results['dod']
        ah = batt_results['ah']
        losses=0.5
        nreff=0.5
        #batt capacity
        batt_capacity = round((TED * losses * autonomy) / (nreff* dod * systemvolts))
        print("battery capacity: ", batt_capacity)
        
        #no of strings for the system voltage
        no_battInStrings = batt_capacity / ah
        print("no of strings for the system voltage: ", no_battInStrings)

        # batt in series(string)
        batt_series =systemvolts / battvolts
        print("batt in series(string): ", batt_series)

        #  no of batt
        NoOfbattery = (no_battInStrings * batt_series)
        print("number of battery:  ", NoOfbattery)


        #inverter sezing
        inverter  = round(power *1.1)
        print("inverter sezing: ", inverter)

        my_dict['batt_capacity']=batt_capacity
        my_dict['no_battInStrings']=no_battInStrings
        my_dict['batt_series']=batt_series
        my_dict['noofbattery']= NoOfbattery
        my_dict['inverter']=inverter
        

        #min no of panels in a string to be conected to inverter
        # VmpNew    = Vmpold + (Vcoeff*(Tamb-Tstc))
        # min_panels= (Vmax*1.1)/VmpNew
        # print("min no of panels to inverter: ", min_panels)


        # # max no of panes in a string tobe conected to inverter
        # VocNew=VocOld + (Vcoeff*(Tamb-Tstc))
        # max_panels= (Vmin*0.95)/VocNew
        # print("max panels to inverter: ", max_panels)

        return {'data':my_dict}




