from .. import db
from typing import List
import datetime as dt



class FavouriteModel(db.Model):
    __tablename__ = "favourite"

    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    product_id   = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    timeStamp    = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)
    # user_id   = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default='69')
    
    #relationship
    # user      = db.relationship('UserModel', backref=db.backref('favourites', lazy='joined'))
    product      = db.relationship('ProductModel', backref="favourites")

   

    @classmethod
    def find_all(cls) -> List["FavouriteModel"]:
        return cls.query.all()


    def __repr__(self):
        return self.id


    
