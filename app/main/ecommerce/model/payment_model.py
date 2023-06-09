from typing   import List
from ....main import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = "invoice"

    id                  = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    user_id             = db.Column(db.Integer,  db.ForeignKey('user.id'), nullable=False)
    phoneNumber         = db.Column(db.String,   nullable=False)
    paymentType         = db.Column(db.String,   nullable=False)
    amount              = db.Column(db.Float,    nullable=False)
    date                = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    merchant_request_id = db.Column(db.String(100), nullable=False)

    def __init__(self,user_id, phoneNumber, paymentType,  amount, merchant_request_id):
        self.user_id             = user_id
        self.phoneNumber         = phoneNumber
        self.paymentType         = paymentType
        self.amount              = amount
        self.merchant_request_id = merchant_request_id
        self.date                = datetime.now()

    def save(invoice):
        db.session.add(invoice)
        try:
            db.session.commit()
            return {"status": True}
        except Exception as e:
            return {"status": False, "message": str(e)}

    @classmethod
    def find_all(cls) -> List["Invoice"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id) -> "Invoice":
        return cls.query.filter_by(id=_id).first() 

    @classmethod
    def find_by_userId(cls, userId) -> "Invoice":
        return cls.query.filter_by(user_id= userId).all() 


class Transaction(db.Model):
    __tablename__ = "transaction"

    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    receipt_id          = db.Column(db.String(200), nullable=False)
    transactionDate     = db.Column(db.String(250), nullable=False)
    amount              = db.Column(db.Float, nullable=False)
    user_id             = db.Column(db.Integer,  db.ForeignKey('user.id'), nullable=False)
    merchant_request_id = db.Column(db.String(200), nullable=False)
    phoneNumber         = db.Column(db.String, nullable=False)
    paymentType         = db.Column(db.String,  nullable=False)

    def __init__(self,receipt_id, amount, user_id, merchant_request_id, phoneNumber, paymentType, transactionDate):
        self.receipt_id = receipt_id
        self.amount = amount
        self.transactionDate = transactionDate
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

    @classmethod
    def find_all(cls) -> List["Transaction"]:
        return cls.query.all()

    
    @classmethod
    def find_by_id(cls, _id) -> "Transaction":
        return cls.query.filter_by(id=_id).first() 


    @classmethod
    def find_by_userId(cls, userId) -> "Transaction":
        return cls.query.filter_by(user_id= userId).all() 