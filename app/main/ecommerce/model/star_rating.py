
from  ....main import db
from datetime import datetime
from typing import List

from statistics import mean
# from sqlalchemy import func

class StarRatingModel(db.Model):

    __tablename__ = "starRating"

    id            = db.Column(db.Integer, primary_key=True, )
    rating    =db.Column(db.Integer,)
    rate = db.Column(db.Integer,)
    
    # product_id    = db.Column(db.Integer,db.ForeignKey('product.id'),nullable=False)

    # critic_avg = db.session.query(func.avg(StarRatingModel.rating)).scalar() or 0

    # four_stars =db.Column(db.Integer )
    # three_stars =db.Column(db.Integer, )
    # two_stars=db.Column(db.Integer )
    # one_star=db.Column(db.Integer )
    # count=db.Column(db.Integer ,)
    # total=db.Column(db.Integer ,)
    # rating=db.Column(db.Integer ,)
   
    
   
    
    
    
    def __init__(self,rating,rate):
        self.rating = rating
        self.rate =rate
        # self.four_stars  = four_stars 
        # self.three_stars = three_stars
        # self.two_stars =two_stars
        # self.one_star=one_star
        
    
    def __repr__(self):
        return ' StarRatingModel(name=%s)' % self.rating


    
    

        
      

    def json(self):
        return {
    
        'rating ': self.rating,
        }    
    
    # def sum_rating(cls)-> List ["StarRatingModel"]:
    #     result = cls.query.all()
    #     dict=dict()
    #     # total = sum(d['rating'] for d in result )
    #     num =mean(d['rating'] for d in result)
    #     # list =[12,1,2,3]
    #     # avg= mean(num)
    #     # num.save_to_db()
    #     # print(num)
    #     return num
    # def sum_rating(cls)-> List ["StarRatingModel"]:
    #     result = cls.query.all()
    #     # avg= mean(result)
    #     num=list(result.keys())
    #     return num
    
    @classmethod
    def find_by_id(cls, _id) -> " StarRatingModel":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["StarRatingModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
