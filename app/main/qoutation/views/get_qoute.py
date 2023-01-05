import requests ,json
from app.main import db
from app.main.qoutation.models.dereted_power import DeretedPanel
from app.main.qoutation.models.qoutation_model import Qoute
from app.main.qoutation.models.batt import Batt




from flask                        import request
from flask_restx                  import Resource

from ..schemas.schema             import QouteSchema
from ..utils.dto                  import QouteGetDto


api  =QouteGetDto.api
_getqoute = QouteGetDto.get_qoute


qoute_Schema = QouteSchema()
qoute_list_Schema =  QouteSchema( many=True)

@api.route('/')
class QouteList(Resource):

    @api.doc('list_of_dereted')
    @api.marshal_list_with(_getqoute, envelope='data')
    
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        
        
        
        return qoute_list_Schema.dump(Qoute.find_all()),200
