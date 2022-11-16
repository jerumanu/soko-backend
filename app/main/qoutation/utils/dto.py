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

    api = Namespace('dereted', description='comments related operations')
    dereted= api.model('dereted', { 

        'name': fields.String(description='locations of the client'),
        'tstc': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'wp': fields.Integer(required=True, description='No of days the battrey takes to be fuly discharged'),
        'vmp':fields.Integer( required=True, description=' latitude logations of the client  '),
        'voc':fields.Integer( required=True, description=' longtitude logations of the client  '),
        'isc':fields.Integer( required=True, description=' client prefrence system volts'    ),
        'tcoeff':fields.Integer( required=True, description=' client prefrence system volts'    ) ,
        'fman':fields.Integer( required=True, description=' client prefrence system volts'    ) ,
        'vcoeff':fields.Integer( required=True, description=' client prefrence system volts'    ) ,

        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })
class BattDto:

    api = Namespace('batt', description='comments related operations')
    batt= api.model('dereted', { 

        'name': fields.String(description='locations of the client'),
        'battv': fields.Integer(required=True, description='total energy demand in kw/hrs'),
        'dod': fields.Integer(required=True, description='No of days the battrey takes to be fuly discharged'),
        'ah':fields.Integer( required=True, description=' latitude logations of the client  '),
        # 'voc':fields.Integer( required=True, description=' longtitude logations of the client  '),
        

        # 'date_added ':fields.DateTime( required=True, description=' date created'    )
    })


