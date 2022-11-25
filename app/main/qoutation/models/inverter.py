from typing import List
from  ... import db
from datetime import datetime





class Inverter(db.Model):

    __tablename__="inveter"


    id  = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name= db.Column(db.String(50) ,unique=True)
    vmin= db.Column(db.Integer,)
    vmax= db.Column(db.Integer,)
    max_panels = db.Column(db.Integer)
    min_panels = db.Column(db.Integer)
    

   
    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self,name, vmin,vmax,max_panels,min_panels,panel_name):

        self.vmax = vmax
        self.name=name
        self.vmin = vmin
        self.max_panels =max_panels
        self.min_panels = min_panels
        self.panel_name = panel_name


        
        
        
    
    

    def __repr__(self):
        return 'Inverter (name=%s)' % self.name

    def json(self):
        return {'name': self.name, }   

    @classmethod
    def find_by_name(cls, name) -> "Inverter ":
        return cls.query.filter_by(name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "Inverter ":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["Inverter "]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()












