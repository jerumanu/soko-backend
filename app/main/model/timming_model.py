from datetime import time
from .. import db 
from typing import List

# class TimeFormat(fields.Raw):
#     def format(self, value):
#         return time.strftime(value, "%H:%M")

class TimeFormat(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time= db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    closed_all_day= db.Column(db.Boolean())


    @classmethod
    def find_by_id(cls, _id) -> "TimeFormat":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["TimeFormat"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
