from flask_restx import Namespace, fields


class LoadsDto:

    api = Namespace('loads', description='comments related operations')
    loads= api.model('loads', { 

        'tenegerydemand': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'autonomy': fields.Integer(required=True, description='No of days the battrey takes to be fuly discharged'),
        'location': fields.String(description='locations of the client'),
        'latitude':fields.Integer( required=True, description=' latitude logations of the client  '),
        'longtitude':fields.Integer( required=True, description=' longtitude logations of the client  '),
        'systemvolts':fields.Integer( required=True, description=' client prefrence system volts'    )  ,
        # 'date_added ':fields.DateTime( required=True, description=' time the product was updated  ')
    })

class DeretedDto:

    api = Namespace('derated', description='panels details ')
    dereted= api.model('dereted', { 

        

        'name': fields.String(description='locations of the client'),
        'tstc': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'wp': fields.Integer(required=True, description='No of days the battrey takes to be fuly discharged'),
        'vmp':fields.Integer( required=True, description=' latitude logations of the client  '),
        'voc':fields.Integer( required=True, description=' longtitude logations of the client  '),
        'isc':fields.Integer( required=True, description=' client prefrence system volts'    ),
        'tcoeff':fields.Float(0.00,required=True, description='product price'),
        'fman':fields.Float(0.00,required=True, description='product price'),
        'vcoeff':fields.Float(0.00,required=True, description='product price'),
        'dirt':fields.Float(0.00,required=True, description='product price'),
        # 'price'        : fields.Float(0.00,required=True, description='product price'),



        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })
class BattDto:

    api = Namespace('batt', description='comments related operations')
    batt= api.model('batt', { 

        'batt_name': fields.String(description='locations of the client'),
        'battv': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'dod':  fields.Float(0.00,required=True, description='product price'),
        'ah':fields.Integer( required=True, description=' latitude logations of the client  '),
        'losses' : fields.Float(0.00,required=True, description='product price'),
        'nreff':fields.Float(0.00,required=True, description='product price')

        # 'voc':fields.Integer( required=True, description=' longtitude logations of the client  '),
        

        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })

class QouteDto:

    api = Namespace('qoute', description=' qoute user realted details ')
    qoute= api.model('qoute', { 

        'ap_demand': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'ligth_demand': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'name_panel':fields.String( description='locations of the client'),
        'batt_name':fields.String( description='locations of the client'),
        'autonomy': fields.Integer(required=True, description='No of days the battrey takes to be fuly discharged'),
        'location': fields.String(description='locations of the client'),
        'latitude':fields.Integer( required=True, description=' latitude logations of the client  '),
        'longtitude':fields.Integer( required=True, description=' longtitude logations of the client  '),
        'systemvolts':fields.Integer( required=True, description=' client prefrence system volts')  ,
        'kw':fields.Integer( required=True, description=' client prefrence system volts')  ,
        
    })
class QouteGetDto:

    api = Namespace('get_qoute', description=' qoute user realted details ')
    get_qoute= api.model('get_qoute', { 

        'ap_demand': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'ligth_demand': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'name_panel':fields.String( description='locations of the client'),
        'batt_name':fields.String( description='locations of the client'),
        'autonomy': fields.Integer(required=True, description='No of days the battrey takes to be fuly discharged'),
        'location': fields.String(description='locations of the client'),
        'latitude':fields.Integer( required=True, description=' latitude logations of the client  '),
        'longtitude':fields.Integer( required=True, description=' longtitude logations of the client  '),
        'systemvolts':fields.Integer( required=True, description=' client prefrence system volts')  ,
        'kw':fields.Integer( required=True, description=' client prefrence system volts')  ,
        'power': fields.Integer( description='total energy demand in kw/hrs'),
        'panel': fields.Integer( description='No of days the battrey takes to be fuly discharged'),
        'panels_series':fields.Integer(  description=' latitude logations of the client  '),
        'total_panels':fields.Integer(  description=' longtitude logations of the client  '),
        'charge_controler':fields.Integer(  description=' longtitude logations of the client  '),
        'batt_capacity':fields.Integer(  description=' longtitude logations of the client  '),
        'batt_string':fields.Integer(  description=' longtitude logations of the client  '),
        'batt_series':fields.Integer(  description=' longtitude logations of the client  '),
        'no_batt':fields.Integer(  description=' longtitude logations of the client  '),
        'inverter':fields.Integer(  description=' longtitude logations of the client  '),
        'panels_parallel':fields.Integer(  description=' longtitude logations of the client  '),
        'h_string_p':fields.Integer(  description=' longtitude logations of the client  '),
        'l_string_p':fields.Integer(  description=' longtitude logations of the client  '),
        'iccc':fields.Integer(  description=' longtitude logations of the client  '),
        'wpd':fields.Integer(  description=' longtitude logations of the client  '),
        'grid_inverter':fields.Integer(  description=' longtitude logations of the client  '),
        # 'batt_name':fields.Integer(  description=' longtitude logations of the client  '),

        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })
    
class InverterDto:

    api = Namespace('inverter', description='inverter details ')
    inverter= api.model('inverter', { 
        'name': fields.String(description='locations of the client'),

        'name_panel': fields.String(description='locations of the client'),
        'vmin': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'vmax': fields.Integer(required=True, description='No of days the battrey takes to be fuly discharged'),
        # 'min_panels':fields.Integer( required=True, description=' latitude logations of the client  '),
        # 'max_panels':fields.Integer( required=True, description=' longtitude logations of the client  '),

        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })

class VoltsDropDto:

    api = Namespace('dropdown', description='comments related operations')
    dropdown= api.model('dropdown', { 

        'cable': fields.String(description='locations of the client'),
        # 'rho':fields.Float(0.00,required=True, description='product price'),
        'length':fields.Integer( required=True, description=' latitude logations of the client  '),
        'systemvolts':fields.Integer( required=True, description=' latitude logations of the client '),
        'name_panel':fields.String(description='locations of the client'),
        # 'voc':fields.Integer( required=True, description=' longtitude logations of the client  '),
        

        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })
class CableDropDto:

    api = Namespace('cables details', description='cables rho info')
    cable= api.model('cable', { 

        'cable': fields.String(description='locations of the client'),
        'rho':fields.Float(0.00,required=True, description='product price'),
        
        # 'voc':fields.Integer( required=True, description=' longtitude logations of the client  '),
        

        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })