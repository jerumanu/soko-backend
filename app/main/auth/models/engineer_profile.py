from typing import List
from  ....main import db
from datetime import datetime
# from .user import User
import enum




class Engineer(db.Model):

    __tablename__="engineer"

    id            = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    engineerUser  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    profesion     = db.Column(db.String(250), nullable=False)
    specification = db.Column(db.String(250), nullable=False)
    location      = db.Column(db.String(150), nullable=False)
    phoneNumber   = db.Column(db.String(150), nullable=False)
    website       = db.Column(db.String(200), nullable=True)
    linkdin       = db.Column(db.String(200), nullable=True)
    twitter       = db.Column(db.String(200), nullable=True)
    instagram     = db.Column(db.String(200), nullable=True)
    date_added    = db.Column(db.DateTime(),  default=datetime.utcnow, onupdate=datetime.utcnow )
  

    def __init__(self,profesion,specification,location,phoneNumber,website,linkdin,twitter,instagram,  engineerUser):

        self.profesion     = profesion
        self.specification = specification
        self.location      = location
        self.phoneNumber   = phoneNumber
        self.website       = website
        self.linkdin       = linkdin
        self.twitter       = twitter
        self.instagram     = instagram
        self.date_added    = datetime.now()
        self.engineerUser  = engineerUser

        
        
    def __repr__(self):
        return 'Engineerl(location=%s)' % self.location

    def json(self):
        return {'location': self.location, }   

    # @classmethod
    # def find_by_name(cls, name) -> "Engineer":
    #     return cls.query.join(User).filter(User.firstname==name or User.lastname==name).all()

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









    