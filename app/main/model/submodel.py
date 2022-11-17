from .. import db
from typing import List
import datetime as dt


class SolarType(db.Model):
    __tablename__ = "solarType"

    id   = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    createAt    = db.Column(db.DateTime, nullable=False, default=dt.datetime.now())

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.createAt    = dt.datetime.now()
        self.name        = name
      


    @classmethod
    def find_all(cls) -> List["SolarType"]:
        return cls.query.all()



class Brand(db.Model):
    __tablename__ = "brand"

    id   = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    createAt    = db.Column(db.DateTime, nullable=False, default=dt.datetime.now())

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.createAt    = dt.datetime.now()
        self.name        = name

    @classmethod
    def find_all(cls) -> List["Brand"]:
        return cls.query.all()

