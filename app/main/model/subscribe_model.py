from .. import db
from typing import List
import datetime as dt


class SubscribeModel(db.Model):
    __tablename__ = "subscribe"

    id          = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    email       = db.Column(db.String(255), unique=True, nullable=False)
    createdAt   = db.Column(db.DateTime, nullable=False, default=dt.datetime.now())

    def __init__(self, email):
        self.createdAt  = dt.datetime.now()
        self.email      = email

    def __repr__(self) -> str:
        return 'Subscribe(name=%s)' % self.email

    
    @classmethod
    def find_all(cls) -> List["SubscribeModel"]:
        return cls.query.all()

    @classmethod
    def find_by_email(cls, email) -> "SubscribeModel":
        return cls.query.filter_by(email=email)

    


    
    