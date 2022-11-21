from datetime import datetime
from typing import List

from  ....main import db




class CommentsModel(db.Model):

    __tablename__ = "comments"

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on    = db.Column(db.DateTime, nullable=False)
    comment       = db.Column(db.String(250),nullable=False )
    comment_owner  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    update_at     = db.Column(db.DateTime(),default=datetime.utcnow )
    product_id    = db.Column(db.Integer,db.ForeignKey('product.id'),nullable=False)
    


    def __init__(self, created_on ,comment,update_at):
        
        self.created_on  = created_on 
        self.comment = comment
        self.update_at = update_at
        
        
    
    def __repr__(self):
        return 'CommentsModel(comment=%s,product_id=%s,)' % (self.comment ,self.product_id,)

    def json(self):
        return {'comment': self.comment, 'product_id': self.product_id}
    
    @classmethod
    def find_by_id(cls, _id) -> "CommentsModel":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["CommentsModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
