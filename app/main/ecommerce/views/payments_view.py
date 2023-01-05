from app.main                     import db
from app.main.ecommerce.model.payment_model import Invoice, Transaction
from flask                        import request
from flask_restx                  import Resource
from ..schema.schema              import InvoiceSchema
from ..utils.dto                  import InvoiceDto
from app.main                     import mpesa_api
from datetime                     import datetime
from app.main.auth.models.user      import User

api                   =  InvoiceDto.api
_payments             =  InvoiceDto.payment
Payment_NOT_FOUND     = "Payment not found."
payments_schema       =  InvoiceSchema()
payments_list_schema  =  InvoiceSchema(many=True)





@api.route('/')
class payments(Resource):
    @api.doc('all  payments ')
    @api.marshal_list_with(_payments, envelope='data')
    def get(self):
        payment_data = Invoice.find_all()
        if payment_data:
            return payments_list_schema .dump(payment_data),200
        return {'message': Payment_NOT_FOUND}, 404

@api.route('/<int:id>')
class InvoiceId(Resource):
    @api.doc('')
    @api.marshal_with(_payments)
    def get(self, id):
        invoice = Invoice.find_by_id(id)
        if invoice:
            return payments_schema.dump(invoice)
        return {'message': Payment_NOT_FOUND }, 404


@api.route('/user/<int:userId>')
class Invoices(Resource):
    @api.doc('')
    @api.marshal_with(_payments)
    def get(self, userId):
        invoice = Invoice.find_by_userId(userId)
        if invoice:
            return payments_schema.dump(invoice)
        return {'message': Payment_NOT_FOUND }, 404



@api.route('/transact/mpesaexpress')
class Payment(Resource):
    @api.expect(_payments, validate=True)
    def post(self):
        post_data   = request.get_json(force=True)
        phoneNumber = post_data['phoneNumber']
        amount      = post_data['amount']
        paymentType = post_data['paymentType']
        user_id     = post_data['user_id']
        author      = User.query.filter_by(id=post_data['user_id']).first()

        if author:
            data = {
                "business_shortcode": "174379",
                "passcode"          :  "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
                "amount"            : f"{amount}", 
                "phone_number"      : f"{phoneNumber}",
                "reference_code"    : "SokoSolar",
                "callback_url"      : "https://db91-41-90-46-163.ngrok.io/payment/mpesa/callback-url", 
                "description"       : f"Payment for our services" 
            }
        
            resp    = mpesa_api.MpesaExpress.stk_push(**data)
            print(resp)
        
            invoice = Invoice(user_id=user_id, merchant_request_id=resp['MerchantRequestID'], paymentType=paymentType, amount=amount, phoneNumber=phoneNumber)
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
        else: 
            return {"message": "Invalid user ID"}, 404



@api.route('/mpesa/callback-url')
class Payment(Resource):
    def post(self):
        post_data = request.get_json(force=True)
        invoice = Invoice.query.filter_by(merchant_request_id = post_data["Body"]["stkCallback"]["MerchantRequestID"]).first()
        result_code=post_data["Body"]["stkCallback"]["ResultCode"]
        print(post_data)
        if result_code != 0:
            return False

        receipt_id      = post_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        print("receipt_id", receipt_id)
        phoneNumber     = post_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
        transactionDate = post_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
        amount = invoice.amount      
        user_id = invoice.user_id
        paymentType =invoice.paymentType
       
        

        transaction = Transaction(receipt_id=receipt_id, transactionDate=transactionDate, amount=amount, user_id=user_id, merchant_request_id=invoice.merchant_request_id,  phoneNumber=phoneNumber,  paymentType=paymentType)

        print("transaction", transaction.receipt_id)
        
        recorded_transaction = transaction.save()
        print("transaction 2", recorded_transaction.values())


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

        






       
    
    