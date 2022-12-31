from flask_marshmallow       import Marshmallow
from ..model.product_model   import ProductModel
from ..model.subscribe_model import SubscribeModel
from ..model.category_model  import CategoryModel
from ..model.faq_model       import FaqModel
from ..model.blog_model      import BlogModel
from ..model.favourite_model import FavouriteModel
from ..model.product_model   import ProductModel
from ..model.comment_model   import CommentsModel
from ..model.timming_model   import TimeFormat
from ..model.star_rating     import  StarRatingModel
from marshmallow             import EXCLUDE
from  ....main               import db
from ..model.payment_model   import Invoice, Transaction
from ..model.submodel        import SolarType, Brand
ma = Marshmallow()
from marshmallow import Schema, fields


class CommentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentsModel
        load_instance = True
        load_only = ("comments")
        include_fk= True                    

class ProductSchema(ma.SQLAlchemyAutoSchema):
    comment = ma.Nested(CommentsSchema, many=True)
    class Meta:
        model = ProductModel
        load_instance = True
        load_only = ("product")
        include_fk= True

#SQLAlchemyAutoSchema: automatically generate field for model's column
class SubscribeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = SubscribeModel
        
        load_instance = True #optional: deserialize to model instance
        load_only     = ("subscribe")
        include_fk    = True
        # avg_rate = fields.Method("rate")

        # def rate(self):
        #     # result= star_list_schema .dump( StarRatingModel.find_all())
        #     # result=[1,2,3,4,]
        #     # print(result)
        #     # num=mean(result
        #     # )
        #     # data=[]
        #     # num=mean(d['rating'] for d in result)
        #     # print("hello world")
        #     # print(num)
        #     # return num
        #     pass

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = CategoryModel
        load_instance = True #optional: deserialize to model instance
        load_only     = ("category")
        include_fk    = True

class FaqSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = FaqModel
        load_instance = True #optional: deserialize to model instance
        load_only     = ("faq")
        include_fk    = True


class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = BlogModel
        load_instance = True #optional: deserialize to model instance
        load_only     = ("blog")
        include_fk    = True



class FavouriteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = FavouriteModel
        load_instance = True #optional: deserialize to model instance
        load_only     = ("favourite")
        include_fk    = True



class RatingsSchema(ma.SQLAlchemyAutoSchema):

    
    
    class Meta:
        model = StarRatingModel
        include_fk    = True
        include_fk    = True
        load_instance = True
        
    
    # def rate(self):
        # result=  StarRatingModel.find_all()
        # # result=[1,2,3,4,]
        # # print(result)
        # # num=mean(result)
        # num =mean(d['rating'] for d in result)

        # return num
# star_rating = db.session(StarRatingModel).first()
# star_rating.data = "whatever"
# schema = RatingsSchema()
# schema.dump(star_rating)






        include_fk = True        


class InvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = Invoice
        load_instance = True #optional: deserialize to model instance
        load_only     = ("payment Invoice")
        include_fk    = True

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = Transaction
        load_instance = True #optional: deserialize to model instance
        load_only     = ("payment")
        include_fk    = True


class SolarTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = SolarType
        load_instance = True #optional: deserialize to model instance
        load_only     = ("solarType")
        include_fk    = True


class BrandSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model         = Brand
        load_instance = True #optional: deserialize to model instance
        load_only     = ("brand")
        include_fk    = True
