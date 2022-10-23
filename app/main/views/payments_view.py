from app.main                     import db
from app.main.model.payment_model import Invoice, Transaction
from flask                        import request, jsonify, make_response
from flask_restx                  import Resource
from ..schema.schema              import InvoiceSchema, TransactionSchema
from ..utils.dto                  import InvoiceDto, TransactionDto
from app.main                     import mpesa_api
from datetime                     import datetime

# api                   =  InvoiceDto.api
# _payments             =  InvoiceDto.payment
Payment_NOT_FOUND     = "Payment not found."
payments_schema       =  InvoiceSchema()
payments_list_schema  =  InvoiceSchema(many=True)

api                   =  TransactionDto.api
_tpayments            =  TransactionDto.transaction
tpayments_schema      =  TransactionSchema()
tpayments_list_schema =  TransactionSchema(many=True)



# @api.route('/<int:id>')
# class payments(Resource):
#     @api.doc('specific  payments by id')
#     @api.marshal_with(_payments)
#     def get(self, id):
#         payment_data = Invoice.query.filter_by(id=id).first()
#         if payment_data:
#             return payments_schema.dump(payment_data)
#         return {'message': Payment_NOT_FOUND}, 404
    



# @api.route('/user/<int:id>')
# class payments(Resource):
#     @api.doc('specific  payments by user id')
#     @api.marshal_with(_payments)
#     def get(self, user_id):
#         payment_data = Invoice.query.filter_by(user_id=user_id).all()
#         if payment_data:
#             return payments_list_schema.dump(payment_data)
#         return {'message': Payment_NOT_FOUND}, 404





@api.route('/transact/mpesaexpress')
class Payment(Resource):
    @api.expect(_tpayments, validate=True)
    def post(self):
        post_data   = request.get_json(force=True)
        phoneNumber = post_data['phoneNumber']
        amount      = post_data['amount']
        paymentType = "test" 
        # user_id     = post_data['userId']
        user_id     = 1
        print(post_data)

        data = {
            "business_shortcode": "174379",
            "passcode"          : "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
            "amount"            : f"{amount}", 
            "phone_number"      : f"{phoneNumber}",
            "reference_code"    : "Payment test",
            "callback_url"      : "https://b4b8-105-163-22-34.ngrok.io/payment/mpesa/callbackUrl", 
            "description"       : f"Payment for our services" 
        }
        print(data)

        resp    = mpesa_api.MpesaExpress.stk_push(**data)
        invoice = Invoice(user_id, resp['MerchantRequestID'], paymentType, amount)
        saved_invoice = invoice.save()

        if saved_invoice["status"]:
            return{
                'status': 'success', 
                'merchantRequestId': resp['MerchantRequestID']
            },200

        else:
            return{
                'status': 'fail', 
                'message': saved_invoice["message"]
            }, 500


@api.route('/mpesa/callbackUrl', methods=["POST"])
class mpesaCallBack(Resource):
    # @api.expect(_tpayments, validate=True)
    def post(self):
        post_data = request.get_json(force=True)
        invoice = Invoice.query.filter_by(merchant_request_id = post_data["Body"]["stkCallback"]["MerchantRequestID"]).first()
        result_code=post_data["Body"]["stkCallback"]["ResultCode"]
        print(post_data)
        if result_code != 0:
            return False

        mpesa_receipt = post_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        date_paid = datetime.now()
        amount = invoice.amount      
        # campaign_id = invoice.campaign_id
        user_id = invoice.user_id

        transaction = Transaction(mpesa_receipt, date_paid, amount,user_id, invoice.merchant_request_id)
        recorded_transaction = transaction.save()

        if recorded_transaction["status"]:
            return True


@api.route('/mpesa/verify', methods=["POST"])
class MpesaVerification(Resource):
    def post(self):
        data = request.get_json(force=True)
        print("--------Data--------")
        print(data)
        if 'merchantRequestId' not in data:
            return {
                    'status' : 'error', 
                    'message': "No invoice found"
                }, 404

        merchant_request_id = data['merchantRequestId']
        transaction = Transaction.query.filter_by(merchant_request_id = merchant_request_id).first()
        
        if not transaction:
            return {
                    'status': 'error', 
                    'message': "No invoice found"
                }, 404

        return {
                'status': 'success'
            }, 200

        






       
    
    