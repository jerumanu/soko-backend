from .. import db 
from datetime import datetime
from typing import List
from .favourite_model import FavouriteModel

class ProductModel(db.Model):

    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_added=db.Column(db.DateTime(),default=datetime.utcnow )
    name = db.Column(db.String(50), unique=True)
    description =db.Column(db.String(250),nullable=False )
    price = db.Column(db.Integer, nullable=False)
    image=db.Column(db.String(256))
    product_owner=db.Column(db.String(50), unique=True)
    
    
    def __init__(self, name,description,product_owner,image,price,date_added):
        self.name          = name
        self.description   = description
        self.image         = image
        self.product_owner = product_owner
        self.price         = price
        self.date_added    = date_added

    def __repr__(self):
        return 'ProductModel(name=%s)' % self.name

    @classmethod
    def find_by_name(cls, name) -> "ProductModel":
        return cls.query.filter_by(name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "ProductModel":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["ProductModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
