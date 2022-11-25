from flask_marshmallow       import Marshmallow

from app.main.qoutation.models.load_analysis import LoadAnalysis
from ..models.dereted_power import DeretedPanel
from ..models.inverter import Inverter
from ..models.qoutation_model import Qoute
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
class QouteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =Qoute
        load_instance = True
        load_only = ("qoute")
        include_fk= True     
        
class InverterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inverter
        load_instance = True
        load_only = ("inverter")
        include_fk= True     
        