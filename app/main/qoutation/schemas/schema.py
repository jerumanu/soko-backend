from flask_marshmallow       import Marshmallow

from app.main.qoutation.models.load_analysis import LoadAnalysis
from ..models.dereted_power import DeretedPanel
# from ...main import db
# from ..views.Star_rating import star_list_schema


ma = Marshmallow()
# from marshmallow import Schema, fields

class LoadsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LoadAnalysis
        load_instance = True
        load_only = ("loads")
        include_fk= True


class DeretedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =DeretedPanel
        load_instance = True
        load_only = ("deretedPanel")
        include_fk= True

class BattSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =DeretedPanel
        load_instance = True
        load_only = ("batt")
        include_fk= True        