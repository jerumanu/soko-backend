from typing import List
from  ....main import db
from datetime import datetime





class  CableDropDown(db.Model):

    __tablename__="cable"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    cable       = db.Column(db.String(50) ,unique=True)
    
    rho = db.Column(db.Float)
    
   

    def __init__(self,cable,rho):

        self.cable =cable     
        self.rho = rho
       
        

        
        # self.vmp= vmp
        # self.date_added=date_added
        
        



    def __repr__(self):
        return 'CableDropDown(cable=%s)' % self.cable

    def json(self):
        return {'cable': self.cable, }   



    @classmethod
    def find_by_id(cls, _id) -> "CableDropDown":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["CableDropDown"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()












