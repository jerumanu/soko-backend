from flask_restx import fields,Namespace

class BusinessDto():
        api = Namespace('business', description=' user related operations')
        business = api.model('business', {
                'id'               : fields.Integer(readonly= True, description="unique identifier"),
                'business_name'    : fields.String(required=True, description='business name'),
                'business_owner'   : fields.Integer(required=True, description='business owner'),
                'business_desc'    : fields.String(required=True, description='business desc'),
                'specific_location': fields.String(required=True, description='specific_location'),
                'to_hour'          : fields.String(required=True, description='to_hour'),
                'weekday'          : fields.String(required=True, description='weekday'),
                'from_hour'        : fields.String(required=True, description='from_hour')
             
        })

class EngineerDto():
        api = Namespace('engineer', description=' user related operations')
        engineer = api.model('engineer', {
                'id'           : fields.Integer(readonly= True, description="unique identifier"),
                'profesion'    : fields.String(required=True, description='Your Profession'),
                'engineerUser' : fields.Integer(required=True, description='User id'),
                'specification': fields.String(required=True, description='Your specialization'),
                'phoneNumber'  : fields.String(required=True, description='phoneNumber'),
                'location'     : fields.String(required=True, description='Areas You operate'),
                'website'      : fields.String( description='website link If any'),
                'linkdin'      : fields.String( description='linkdin link if any'),
                'twitter'      : fields.String( description='twitter link if any'),
                'instagram'    : fields.String( description='instagram link if any')

        })   
