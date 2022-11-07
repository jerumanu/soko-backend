from typing import List
from  ....main import db
from datetime import datetime




class LoadAnalysis(db.Model):

    __tablename__=" loads"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    tenegerydemand= db.Column(db.Integer,)
    autonomy = db.Column(db.Integer)
    location=db.Column(db.Integer,)
    latitude = db.Column(db.Integer,)
    longtitude= db.Column(db.Integer)
    date_added=db.Column(db.Datetime)
    update_at     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self, tenegerydemand,autonomy,location,latitude,longtitude,date_added):
        self.tenegerydemand = tenegerydemand
        self.autonomy = autonomy
        self.location= location
        self.latitude=latitude
        self.longtitude=longtitude
        self.date_added=date_added
        
        
    
    

    def __repr__(self):
        return 'LoadAnalysisl(location=%s)' % self.location

    def json(self):
        return {'location': self.location, }   

    @classmethod
    def find_by_name(cls, name) -> "LoadAnalysis":
        return cls.query.filter_by(name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "LoadAnalysis":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["LoadAnalysis"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
