from typing import List
from  ....main import db
from datetime import datetime





class DeretedPanel(db.Model):

    __tablename__="dereted"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True )
    name= db.Column(db.String(50) ,unique=True)
    wp= db.Column(db.Integer,)
    tstc = db.Column(db.Integer)
    vmp=db.Column(db.Integer,)
    voc= db.Column(db.Integer,)
    isc= db.Column(db.Integer)
    tcoeff= db.Column(db.Integer)
    fman=db.Column(db.Integer)
    vcoeff= db.Column(db.Integer)
    wpd= db.Column(db.Integer)

    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self,name, tstc,wp,vmp,voc,isc,tcoeff,fman,vcoeff,wpd):
        self.tstc = tstc
        self.name=name
        self.wp = wp
        self.vmp= vmp
        self.voc=voc
        self.isc=isc
        self.tcoeff=tcoeff
        self.fman=fman
        self.vcoeff =vcoeff
        self.wpd = wpd
        # self.date_added=date_added
        
        
    
    

    def __repr__(self):
        return 'DeretedPanel(name=%s)' % self.name

    def json(self):
        return {'name': self.name, }   

    @classmethod
    def find_by_name(cls, name) -> "DeretedPanel":
        return cls.query.filter_by(name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "DeretedPanel":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["DeretedPanel"]:
        return cls.query.all()


    # def save(dereted):

    #     db.session.add(dereted)
    #     try:
    #         db.session.commit()
    #         return {"status": True}
    #     except Exception as e:
    #         return {"status": False, "message": str(e)
    #         }

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()












