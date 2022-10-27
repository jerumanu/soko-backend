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

ma = Marshmallow()


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



class TimeSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = TimeFormat
        load_instance = True
        include_fk = True        
