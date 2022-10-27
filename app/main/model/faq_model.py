from .. import db
from typing import List
import datetime as dt


class FaqModel(db.Model):
    __tablename__ = "Faq"

    id          = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title       = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    createdAt   = db.Column(db.DateTime, nullable=False, default=dt.datetime.now())

    def __init__(self, title, description):
        self.createdAt   = dt.datetime.now()
        self.title       = title
        self.description = description

    def __repr__(self) -> str:
        return 'Faq(name=%s)' % self.title

    
    @classmethod
    def find_all(cls) -> List["FaqModel"]:
        return cls.query.all()

   
