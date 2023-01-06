from app.main                     import db
from app.main.ecommerce.model.payment_model import  Transaction
from flask                        import request, jsonify, make_response
from flask_restx                  import Resource
from ..schema.schema              import TransactionSchema
from ..utils.dto                  import TransactionDto
from app.main                     import mpesa_api
from datetime                     import datetime
from app.main.auth.extensions.auth.api_doc_required import permission



api                   =  TransactionDto.api
_tpayments            =  TransactionDto.transaction
tpayments_schema      =  TransactionSchema()
tpayments_list_schema =  TransactionSchema(many=True)
Payment_NOT_FOUND     = "Payment not found."


@api.route('/')
class Transactions(Resource):
    @permission
    @api.doc('geting all transaction')
    @api.marshal_list_with(_tpayments , envelope='transaction')
    def get(self):
        return tpayments_list_schema.dump(Transaction.find_all()), 200


@api.route('/<int:id>')
class TransactionId(Resource):
    @permission
    @api.doc('getting transaction by id')
    @api.marshal_with(_tpayments)
    def get(self, id):
        transaction = Transaction.find_by_id(id)
        if transaction:
            return tpayments_schema.dump(transaction)
        return {'message': Payment_NOT_FOUND }, 404

@api.route('/user/<int:userId>')
class TransactionUserId(Resource):
    @permission
    @api.doc('getting transcation by user id')
    @api.marshal_with(_tpayments)
    def get(self, userId):
        transaction = Transaction.find_by_userId(userId)
        if transaction:
            return tpayments_schema.dump(transaction)
        return {'message': Payment_NOT_FOUND }, 404

