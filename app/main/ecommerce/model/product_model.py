from  ....main import db 
from datetime import datetime
from typing import List
import datetime as dt





class ProductModel(db.Model):
    __tablename__ = "product"

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_added    = db.Column(db.DateTime(),default=datetime.utcnow )
    name          = db.Column(db.String(50), unique=True)
    description   = db.Column(db.String(250),nullable=False )
    price         = db.Column(db.Float, nullable=False)
    image         = db.Column(db.String(256))
    product_owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    inStock       = db.Column(db.Boolean,  nullable=False)
    condition     = db.Column(db.String,  nullable=False)
    update_at     = db.Column(db.DateTime(),default=datetime.utcnow )
    category_id   = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    solarType_id  = db.Column(db.Integer, db.ForeignKey('solarType.id'), nullable=False)
    brand_id      = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)


    #relationship
    favourite     = db.relationship('FavouriteModel', backref='product', cascade = 'all, delete-orphan', lazy='joined')
    comment       = db.relationship('CommentsModel', backref='product', cascade = 'all, delete-orphan', lazy='joined')
    ratings       = db.relationship('StarRatingModel', backref='product', cascade = 'all, delete-orphan', lazy='joined')

    



    def __init__(self, name,description,product_owner,image,price, solarType_id, brand_id, condition, inStock, category_id):
        self.name = name
        self.description = description
        self.image = image
        self.product_owner = product_owner
        self.price = price
        self.brand_id = brand_id
        self.solarType_id = solarType_id
        self.condition = condition
        self.inStock  = inStock
        self.category_id = category_id
        self.date_added= dt.datetime.now()
        self.update_at= dt.datetime.now()
        
    
    
    def __repr__(self):
        return 'ProductModel(name=%s)' % self.name

    def json(self):
        return {'price ': self.price , 'price': self.price}    

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
