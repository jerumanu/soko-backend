from flask_restx import fields,Namespace

class BusinessDto():
        api = Namespace('business', description=' user related operations')
        business = api.model('business', {
                'business_name': fields.String(required=True, description='user email address'),
                'business_desc': fields.String(required=True, description='user username'),
                'specific_location': fields.String(required=True, description='user password'),
                'location': fields.String(required=True, description='user password'),
                # 'date_added ':fields.DateTime( required=True, description=' date created'    )
})

class EngineerDto():
        api = Namespace('engineer', description=' user related operations')
        engineer = api.model('engineer', {
                'profesion': fields.String(required=True, description='user email address'),
                'specification': fields.String(required=True, description='user username'),
                'number': fields.Integer(required=True, description='user password'),
                'location': fields.String(required=True, description='user password'),
                'website': fields.String( description='user password'),
                'linkdin': fields.String( description='user password'),
                'twitter': fields.String( description='user password'),
                'instagram': fields.String( description='user password'),

                # 'date_added ':fields.DateTime( required=True, description=' date created'    )

})   
