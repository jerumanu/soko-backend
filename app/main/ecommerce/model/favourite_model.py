from  ....main import db
from typing import List
import datetime as dt



class FavouriteModel(db.Model):
    __tablename__ = "favourite"

    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    product_id   = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    timeStamp    = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    @classmethod
    def find_all(cls) -> List["FavouriteModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id) -> "FavouriteModel":
        return cls.query.filter_by(id=_id).first() 


    def __repr__(self):
        return self.id



