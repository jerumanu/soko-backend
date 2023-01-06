from typing import List
from  ....main import db
from datetime import datetime
from ...auth.models.user import User



class Qoute(db.Model):

    __tablename__=" qoute"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    qoute_owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tenegerydemand= db.Column(db.Integer,)
    autonomy = db.Column(db.Integer)
    location=db.Column(db.String(50),)
    latitude = db.Column(db.Integer,)
    longtitude= db.Column(db.Integer)
    systemvolts=db.Column(db.Integer)
    name_panel =db.Column(db.String(20))
    power= db.Column(db.Integer,)
    panel = db.Column(db.Integer)
    panels_series=db.Column(db.Integer)
    panels_parallel=db.Column(db.Integer)
    total_panels = db.Column(db.Integer,)
    charge_controller= db.Column(db.Integer)
    batt_capacity=db.Column(db.Integer)
    batt_string = db.Column(db.Integer)
    batt_series =db.Column(db.Integer)
    no_batt =db.Column(db.Integer)
    inverter =db.Column(db.Integer)
    batt_name = db.Column(db.String(50))
    kw = db.Column(db.Integer)
    grid_inverter=db.Column(db.Integer)
    l_string_p=db.Column(db.Integer)
    h_string_p=db.Column(db.Integer)
    iccc=db.Column(db.Integer)
    wpd=db.Column(db.Integer)


    


    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self,power ,product_owner, panel,panels_series,total_panels,charge_controller,kw,grid_inverter,iccc,l_string_p,h_string_p,
        batt_capacity,batt_string,batt_series,no_batt,inverter,tenegerydemand,autonomy,systemvolts,location,wpd,panels_parallel,
        latitude,batt_name,name_panel,longtitude):


        self.tenegerydemand = tenegerydemand
        self.autonomy = autonomy
        self.location= location
        self.latitude=latitude
        self.longtitude=longtitude
        self.name_panel=name_panel
        self.systemvolts=systemvolts
        self.power = power
        self.panel =panel
        self.panels_series =panels_series
        self.total_panels = total_panels
        self.charge_controller =charge_controller
        self.batt_capacity = batt_capacity
        self.batt_string = batt_string
        self.batt_series = batt_series
        self.no_batt =no_batt
        self.inverter = inverter
        self.batt_name = batt_name
        self.kw = kw
        self.grid_inverter= grid_inverter
        self.l_string_p=l_string_p
        self.h_string_p=h_string_p
        self.iccc=iccc
        self.wpd=wpd
        self.panels_parallel=panels_parallel
        self.product_owner = product_owner





        
    
    

    def __repr__(self):
        return 'Qoutel(power=%s)' % self.power

    def json(self):
        return {'power': self.power, }   

    @classmethod
    def find_by_name(cls, name) -> "Qoute":
        return cls.query.filter_by(name = name).first()
    # delete_user = cls.query.filter_by( user_id == User.id).first() 

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
