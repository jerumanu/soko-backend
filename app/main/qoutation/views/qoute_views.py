import requests
from app.main import db
from app.main.qoutation.models.dereted_power import DeretedPanel
from app.main.qoutation.models.load_analysis import LoadAnalysis
from app.main.qoutation.models.batt import Batt




from flask                        import request
from flask_restx                  import Resource

from ..schemas.schema             import DeretedSchema,LoadsSchema,BattSchema,QouteSchema
from ..utils.dto                  import DeretedDto ,QouteDto





api  =QouteDto.api
_qoute  = QouteDto.qoute



ITEM_NOT_FOUND = "Dereted panel power not found  not found."


dereted_schema= DeretedSchema()
dereted_list_schema=  DeretedSchema(many=True)

loads_schema = LoadsSchema()
loads_list_schema =  LoadsSchema( many=True)

batt_Schema = BattSchema()
batt_list_Schema =  BattSchema( many=True)

qoute_Schema = QouteSchema()
qoute_list_Schema =  QouteSchema( many=True)





            # self.wpd
            # panels = round(power /wpd)
            # my_cal['wpd']=wpd

            
            

        

        # return results

        
# def panels(self):

#     panels = round(power /wpd)
@api.route('/')
class QouteList(Resource):

    @api.doc('list_of_dereted')
    @api.marshal_list_with(_qoute, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        return dereted_list_schema.dump( DeretedPanel.find_all()), 200

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_qoute , validate=True )

    def post(self):

        qoute_json = request.get_json()
        

        

        print("relusts",qoute_json)
        

        lat=qoute_json['latitude']
        lon=qoute_json['longtitude']
        autonomy=qoute_json['autonomy']
        location=qoute_json['location']
        kw = qoute_json ['kw']
        systemvolts = qoute_json ['systemvolts']
        


        payload={'lat':30,'lon':80}

        payload['lat'] = lat

        payload['lon'] = lon

        


        #print(r['inputs']['log'])

        print (payload)

        r=requests.get('https://developer.nrel.gov/api/pvwatts/v6.json?api_key=DEMO_KEY&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10', params=payload).json()





        
        
        print('annual psh of the area',r['outputs']["solrad_annual"])
        print("psh of the area",r['outputs']["solrad_monthly"])

        psh=min(r["outputs"]["solrad_monthly"])



        results = loads_list_schema.dump( LoadAnalysis.find_all())

        name = qoute_json['name_panel']

        
        # ted_name= next(d for d in results if d['name'] == name)

        results1 =dereted_list_schema.dump( DeretedPanel.find_all())

        panel_name= next(d for d in results1 if d['name'] == name)
        # print('rese',results)
        print ("panel_name",panel_name)
        panelsvolts =12
        NUM =0.2
        s_factor=1.1
        print('results1',results)
        
        ted= qoute_json['tenegerydemand']

       

        print (ted)

        # autonomy = results ['autonomy ']
        # location = results['location']
        # latitude = results['latitude']
        # longtitude = results['longtitude']

        




        wpd = panel_name['wpd']
        isc = panel_name['isc']

        power = ted / psh

        print (power)

        panels = round(power / wpd)

        print(panels)

        panels_parallel = round(((panels * panelsvolts) / systemvolts) + NUM)

        series = systemvolts / panelsvolts
        print("no of panel in series: ", series)

        #total panels required

        totalpanels = series * panels_parallel
        print("Final total number of panels: ", totalpanels)

        

        #charge controller

        charge_controller = s_factor * isc * panels_parallel
        print("charge of controller: ", charge_controller)

        batt_name =qoute_json['batt_name'] 
        
        batt_results = batt_list_Schema.dump(Batt.find_all())


        batt_result= next(d for d in batt_results  if d['name'] == batt_name)


        battvolts = batt_result['battv']
        dod = batt_result['dod']
        ah = batt_result['ah']
        # losses = batt_result['losses']
        losses = 0.5
        nreff = 0.5

        #batt capacity

        batt_capacity = round((ted * losses * autonomy) / (nreff* dod * systemvolts))
        print("battery capacity: ", batt_capacity)
        
        #no of strings for the system voltage

        no_batt_strings = batt_capacity / ah
        print("no of strings for the system voltage: ", no_batt_strings)


        # batt in series(string)

        batt_series = systemvolts / battvolts
        print("batt in series(string): ", batt_series)

        #  no of batt

        no_battery = (no_batt_strings * batt_series)

        print("number of battery:  ", no_battery)


        inverter  = round(power *1.1)



        grid_inverter = round(kw*1.1)




        """
        min no of panels in a string to be conected to inverter
        """

        # VmpNew    = Vmpold + (Vcoeff*(Tamb-Tstc))
        # min_panels= (Vmax*1.1)/VmpNew


        # print("min no of panels to inverter: ", min_panels)

        """ 
        max no of panes in a string tobe conected to  inverter 

        """

        # VocNew = VocOld + (Vcoeff*(Tamb-Tstc))


        # max_panels= (Vmin*0.95)/VocNew


        # print("max panels to inverter: ", max_panels)

        '''
        cable sizing
        '''
        # icc= 3

        # cable = icc >= 1.25  * isc_mod * no_string 




        """
        cable protections

        """

        """
        maximun number of  strings  without  string protections 
        """


        # string_protections = 1.5 * isc < fuse_rating > isc  * 2.4 
        


        qoute_json['power'] = power
        qoute_json['panel'] =  panels
        # qoute_json['panels_parallel'] =  panels_parallel
        qoute_json['panels_series'] =  series
        qoute_json['total_panels'] =  totalpanels
        qoute_json['charge_controller'] =  charge_controller

        qoutation_json = dict()

        qoutation_json['power'] = power
        qoutation_json['panel'] =  panels
        # qoutation_json['panels_parallel'] =  panels_parallel
        qoutation_json['panels_series'] =  series
        qoutation_json['total_panels'] =  totalpanels
        qoutation_json['charge_controller'] =  charge_controller
        qoutation_json['systemvolts'] =  systemvolts
        qoutation_json['location'] =  location
        qoutation_json['latitude'] =  lat
        qoutation_json['longtitude'] =  lon
        qoutation_json['name_panel'] =  name
        qoutation_json['batt_capacity'] =  batt_capacity
        qoutation_json['batt_string'] =  no_batt_strings 
        qoutation_json['batt_series'] =  batt_series
        qoutation_json['no_batt'] = no_battery
        qoutation_json['inverter'] =  inverter
        qoutation_json['tenegerydemand'] =  ted
        qoutation_json['autonomy'] =  autonomy
        qoutation_json['batt_name'] =  batt_name

        qoutation_json['kw'] =  kw
        qoutation_json['grid_inverter'] =  grid_inverter

        print('qoutation json',qoutation_json)





        print ('wpd',wpd)

        print('qoute_json', qoute_json)




        qoute_data = qoute_Schema.load(qoutation_json)



        
        qoute_data.save_to_db()

        return qoute_Schema.dump(qoute_data), 201
    

# class Qoute(Resource):
    





#         payload={'lat':40,'lon':-105}

#         payload['lat'] = 30

#         payload['lon'] = 80




#         #print(r['inputs']['log'])

#         print (payload)
#         r=requests.get('https://developer.nrel.gov/api/pvwatts/v6.json?api_key=DEMO_KEY&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10', params=payload).json()


#         print('latitude of the area',
#           r['inputs']['lat'])
        

#         print(r['inputs']['log'])
#         print('annual psh of the area',r['outputs']["solrad_annual"])
#         print("psh of the area",r['outputs']["solrad_monthly"])
#         psh=min(r["outputs"]["solrad_monthly"])



#         results = loads_list_schema.dump( LoadAnalysis.find_all())
        

#         print('results1',results)
#         my_dict['PSH'] = psh
#         ted = results ['tenegerydemand']
#         autonomy = results ['autonomy ']
#         location = results['location']
#         latitude = results['latitude']
#         longtitude = results['longtitude']
#         systemvolts = results['systemvolts']

#         print(ted)
#         print(autonomy)
#         print(location)
#         print(latitude)
#         print(longtitude)
#         print(systemvolts)


#         power = ted / psh

#         print (power)

#         panels = round(power / wpd)

#         print(panels)

#         panels_parallel = round(((panels * panelsvolts) / systemvolts) + num)

#         series = systemvolts / panelsvolts
#         print("no of panel in series: ", series)

#         #total panels required

#         totalpanels = series * panels_parallel
#         print("Final total number of panels: ", totalpanels)

        

#         #charge controller

#         charge_controller = s_factor * isc * panels_parallel
#         print("charge of controller: ", charge_controller)

#         my_dict['power'] = power
#         my_dict['panels'] = panels
#         my_dict['series'] = series
#         my_dict['panels_parallel'] = panels_parallel
#         my_dict['totalpanels'] = totalpanels
#         my_dict['charge_controler'] = charge_controller


#         batt_results = batt_list_Schema.dump(Batt.find_all()), 200

#         battvolts = batt_results['battv']
#         dod = batt_results['dod']
#         ah = batt_results['ah']
#         losses = 0.5
#         nreff = 0.5

#         #batt capacity

#         batt_capacity = round((ted * losses * autonomy) / (nreff* dod * systemvolts))
#         print("battery capacity: ", batt_capacity)
        
#         #no of strings for the system voltage

#         no_batt_strings = batt_capacity / ah
#         print("no of strings for the system voltage: ", no_batt_strings)


#         # batt in series(string)

#         batt_series = systemvolts / battvolts
#         print("batt in series(string): ", batt_series)

#         #  no of batt

#         no_battery = (no_batt_strings * batt_series)

#         print("number of battery:  ", no_battery)



#         #inverter sezing

#         inverter  = round(power *1.1)

#         print("inverter sezing: ", inverter)

#         my_dict['batt_capacity'] = batt_capacity
#         my_dict['no_battInStrings'] = no_batt_strings
#         my_dict['batt_series'] = batt_series
#         my_dict['noofbattery'] = no_battery
#         my_dict['inverter'] = inverter
        


#         #min no of panels in a string to be conected to inverter
#         # VmpNew    = Vmpold + (Vcoeff*(Tamb-Tstc))
#         # min_panels= (Vmax*1.1)/VmpNew
#         # print("min no of panels to inverter: ", min_panels)
#         # # max no of panes in a string tobe conected to inverter
#         # VocNew=VocOld + (Vcoeff*(Tamb-Tstc))
#         # max_panels= (Vmin*0.95)/VocNew
#         # print("max panels to inverter: ", max_panels)

#         # return  {'data':my_dict} 