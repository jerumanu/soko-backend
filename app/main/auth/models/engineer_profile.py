from typing import List
from  ....main import db
from datetime import datetime




class Engineer(db.Model):

    __tablename__="engineer"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    profesion= db.Column(db.String(50),)
    specification= db.Column(db.String(50),)
    location=db.Column(db.String(50),)
    number= db.Column(db.Integer,)
    website= db.Column(db.String(100))
    linkdin=db.Column(db.String(100))
    twitter = db.Column(db.String(50),)
    instagram= db.Column(db.String(50),)
    
    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self,profesion,specification,location,number,website,linkdin,twitter,instagram):
        self.profesion =profesion
        self.specification =specification
        self.location =location
        self.number = number
        self.website = website
        self.linkdin = linkdin
        self.twitter =twitter
        self.instagram =instagram

        
        
    def __repr__(self):
        return 'Engineerl(location=%s)' % self.location

    def json(self):
        return {'location': self.location, }   

    @classmethod
    def find_by_name(cls, name) -> "Engineer":
        return cls.query.filter_by(name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "Engineer":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["Engineer"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
