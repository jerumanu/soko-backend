from flask_marshmallow import Marshmallow


from ..model.product_model import ProductModel
from ..model.comment_model import CommentsModel
from ..model.timming_model import TimeFormat

ma = Marshmallow()


class CommentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentsModel
        load_instance = True
        load_only = ("product",)
        include_fk= True                    

class ProductSchema(ma.SQLAlchemyAutoSchema):
    comment = ma.Nested(CommentsSchema, many=True)
    class Meta:
        model = ProductModel
        load_instance = True
        include_fk = True
class TimeSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = TimeFormat
        load_instance = True
        include_fk = True        
