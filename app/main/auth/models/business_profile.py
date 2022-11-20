from typing import List
from  ....main import db
from datetime import datetime




class Business(db.Model):

    __tablename__=" business"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    business_name=db.Column(db.String(50),unique=True)
    # business_owner =db.Column(db.String(50),unique=True)
    business_desc= db.Column(db.String(50))
    specific_location =db.Column(db.String)
    # opening_days=db.Column(db.DateTime(),default=datetime.utcnow )
    # start_time=db.Column(db.DateTime(),default=datetime.utcnow )
    # stoptime = db.Column(db.DateTime(),default=datetime.utcnow )
    location=db.Column(db.String(50),)
    
    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self, business_name,business_desc,specific_location,location):
        self.business_name=business_name
        self.business_desc =business_desc
        self.specific_location = specific_location
        # self.opening_days=opening_days
        # self.start_time =start_time
        # self.stoptime = stoptime
        self.location =location
        
        
    
    

    def __repr__(self):
        return 'Business(location=%s)' % self.location

    def json(self):
        return {'location': self.location, }   

    @classmethod
    def find_by_name(cls, name) -> "Business":
        return cls.query.filter_by(name = name).first() 

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
