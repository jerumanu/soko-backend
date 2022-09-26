from flask_marshmallow import Marshmallow


from ..model.product_model import ProductModel



ma = Marshmallow()






class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        load_only = ("product",)
        include_fk= True