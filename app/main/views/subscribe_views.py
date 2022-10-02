from flask                          import request
from flask_restx                    import Resource
from app.main.model.subscribe_model import SubscribeModel
from app.main.schema.schema         import SubscribeSchema
from app.main.utils.dto             import SubscribeDto
import re
from ..                             import db

regex               = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
api                 = SubscribeDto.api
_subscribe          = SubscribeDto.subscribe
item_schema         = SubscribeSchema()
item_list_schema    = SubscribeSchema( many=True)


@api.route('/subscribe/email')
@api.param('name', 'The User identifier')
class Subscribe(Resource):
    @api.doc('list_of_emails')
    @api.marshal_list_with(_subscribe, envelope='data')
    def get(self):
        return item_list_schema.dump(SubscribeModel.find_all()), 200


    @api.response(201, ' successfully subscribe')
    @api.doc('subscribe to email')
    @api.expect(_subscribe, validate=True)
    def post(self):
        item_json = request.get_json()
        if(re.fullmatch(regex, item_json['email'])):
            emailConfirmation = SubscribeModel.find_by_email(item_json['email'])
            if not emailConfirmation:
                item_data = item_schema.load(item_json)
                db.session.add(item_data)
                db.session.commit()
                return item_schema.dump(item_data), 201
                
            else:
                return {"message": "Email is already subscribed to newsletter"}, 201
        else:
            return {"message": "Invalid Email"}, 404


@api.route('/unsubscribe/<email>')
@api.param('email', 'User email')
class Unsubscribe(Resource):
    @api.doc('unsubscribe by delete the email')
    @api.marshal_with(_subscribe)
    def delete(self, email):
        item_data = SubscribeModel.query.filter_by(email=email.lower()).first()
        if not item_data:
            return {"Email not found"}, 404
        else:
            db.session.delete(item_data)
            db.session.commit()
            return {"Email is unscribed successfully"}
        
        
    @api.doc('get email')
    @api.marshal_with(_subscribe)
    def get(self, email):
        item_data = SubscribeModel.query.filter_by(email=email.lower()).first_or_404(description=f"{email} not found in database.")
        return item_schema.dump(item_data), 200
       

    
       