from flask_marshmallow       import Marshmallow

from app.main.auth.models.business_profile import Business 
from app.main.auth.models.engineer_profile import Engineer
# from ...main import db 



ma = Marshmallow()
# from marshmallow import Schema, fields

class BusinessSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Business
        load_instance = True
        load_only = ("business")
        include_fk= True

class EngineerSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Engineer
        load_instance = True
        load_only = ("engineer")
        include_fk= True   
        