from typing import List
from  ....main import db
from datetime import datetime





class VoltsDropDowm(db.Model):

    __tablename__="dropdown"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    cable = db.Column(db.String(50) ,unique=True)
    isc= db.Column(db.Integer,)
    length=db.Column(db.Integer,)
    systemvolts= db.Column(db.Integer)
    area= db.Column(db.Float)
    name_panel=db.Column(db.String(50))
    # voc= db.Column(db.Integer,)
    # isc= db.Column(db.Integer)
    # tcoeff= db.Column(db.Integer)
    # fman=db.Column(db.Integer)
    # vcoeff= db.Column(db.Integer)
    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self,cable,isc,length,systemvolts,area,name_panel):

        self.cable =cable      
        
        self.length = length
        self.systemvolts=systemvolts
        self.area= area
        self.name_panel=name_panel
        self.isc=isc
        

        
        # self.vmp= vmp
        # self.date_added=date_added
        
        



    def __repr__(self):
        return 'VoltsDropDowm(cable=%s)' % self.cable

    def json(self):
        return {'cable_name': self.cable, }   



    @classmethod
    def find_by_id(cls, _id) -> "VoltsDropDowm":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["VoltsDropDowm"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()












