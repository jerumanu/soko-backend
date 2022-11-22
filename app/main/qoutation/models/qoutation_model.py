from typing import List
from  ....main import db
from datetime import datetime




class Qoute(db.Model):

    __tablename__=" qoute"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    power= db.Column(db.Integer,)
    panel = db.Column(db.Integer)
    panels_series=db.Column(db.Integer)
    
    total_panels = db.Column(db.Integer,)
    charge_controler= db.Column(db.Integer)
    batt_capacity=db.Column(db.Integer)
    batt_string = db.Column(db.Integer)
    batt_series =db.Column(db.Integer)
    no_batt =db.Column(db.Integer)
    inverter =db.Column(db.Integer)


    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self,power , panel,panels_series,total_panels,charge_controler,batt_capacity,batt_string,batt_series,no_batt,inverter):

        self.power = power
        self.panel =panel
        self.panels_series =panels_series
        self.total_panels = total_panels
        self.charge_controler =charge_controler
        self.batt_capacity = batt_capacity
        self.batt_string = batt_string
        self.batt_series = batt_series
        self.no_batt =no_batt
        self.inverter = inverter

       
        
    
    

    def __repr__(self):
        return 'Qoutel(power=%s)' % self.power

    def json(self):
        return {'power': self.power, }   

    @classmethod
    def find_by_name(cls, name) -> "Qoute":
        return cls.query.filter_by(name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "Qoute":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["Qoute"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
