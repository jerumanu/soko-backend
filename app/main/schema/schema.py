from flask_marshmallow import Marshmallow


from ..model.product_model import ProductModel
from ..model.comment_model import CommentsModel


ma = Marshmallow()

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        load_only = ("product",)
        include_fk= True

class CommentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentsModel
        load_instance = True
        load_only = ("store",)
        include_fk= True                    