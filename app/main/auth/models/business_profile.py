from typing import List
from  ....main import db
from datetime import datetime



class Business(db.Model):

    __tablename__="business"


    id                = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)     
    business_name     = db.Column(db.String(50),unique=True)
    business_owner    = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    business_desc     = db.Column(db.String(50), nullable=False)
    specific_location = db.Column(db.String(150), nullable=False)
    date_added        = db.Column(db.DateTime(),  default=datetime.utcnow, onupdate=datetime.utcnow )
    weekday           = db.Column(db.String(250), nullable=False)
    from_hour         = db.Column(db.String(250), nullable=False)
    to_hour           = db.Column(db.String(250), nullable=False)

    def __init__(self, business_name,business_desc,specific_location,business_owner, to_hour, weekday, from_hour):
        self.business_name     = business_name
        self.business_desc     = business_desc
        self.business_owner    = business_owner
        self.specific_location = specific_location
        self.weekday           = weekday 
        self.from_hour         = from_hour
        self.to_hour           = to_hour
        self.date_added        = datetime.now()
  
        
        
    def __repr__(self):
        return 'Business(location=%s)' % self.location

    def json(self):
        return {'location': self.location, }   

    @classmethod
    def find_by_name(cls, name) -> "Business":
        return cls.query.filter_by( business_name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "Business":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["Business"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
