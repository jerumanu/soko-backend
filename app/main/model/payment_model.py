from typing import List
from .. import db 
import datetime as dt

class Invoice(db.Model):
    __tablename__ = "invoice"

    id                  = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    user_id             = db.Column(db.Integer,  db.ForeignKey('user.id'), nullable=False)
    phoneNumber         = db.Column(db.String,   nullable=False)
    paymentType         = db.Column(db.String,   nullable=False)
    amount              = db.Column(db.Float,    nullable=False)
    date                = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self,user_id, phoneNumber, paymentType,  amount):
        self.user_id             = user_id
        self.phoneNumber         = phoneNumber
        self.paymentType         = paymentType
        self.amount              = amount

    def save(invoice):
        db.session.add(invoice)
        try:
            db.session.commit()
            return {"status": True}
        except Exception as e:
            return {"status": False, "message": str(e)}


class Transaction(db.Model):
    __tablename__ = "transaction"

    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    receipt_id          = db.Column(db.String(100), nullable=False)
    date_paid           = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    amount              = db.Column(db.Float, nullable=False)
    user_id             = db.Column(db.Integer,  db.ForeignKey('user.id'), nullable=False)
    merchant_request_id = db.Column(db.String(100), nullable=False)
    phoneNumber         = db.Column(db.String, nullable=False)
    paymentType         = db.Column(db.String,  nullable=False)

    def __init__(self,receipt_id, date_paid, amount, user_id, merchant_request_id, phoneNumber, paymentType):
        self.receipt_id = receipt_id
        self.date_paid = date_paid
        self.amount = amount
        self.user_id = user_id
        self.merchant_request_id = merchant_request_id
        self.phoneNumber = phoneNumber
        self.paymentType = paymentType

    def save(transaction):
        db.session.add(transaction)
        try:
            db.session.commit()
            return {"status": True}
        except Exception as e:
            return {"status": False, "message": str(e)}