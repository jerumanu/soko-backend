from .. import db
from typing import List
import datetime as dt
import pytz



class CategoryModel(db.Model):
    __tablename__ = "category"

    id          = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name        = db.Column(db.String(120), unique=True, nullable=False)
    createdAt   = db.Column(db.DateTime, nullable=False, default=dt.datetime.now())

    def __init__(self, name):
        self.createdAt  = dt.datetime.now()
        self.name       = name

    def __repr__(self) -> str:
        return 'Category(name=%s)' % self.name

    
    @classmethod
    def find_all(cls) -> List["CategoryModel"]:
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name) -> "CategoryModel":
        return cls.query.filter_by(name=name)