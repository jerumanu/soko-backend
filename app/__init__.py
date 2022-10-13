from flask_restx import Api
from flask import Blueprint


from .main.views.products_views import api as products_ns
from .main.views.comment_views import api as comments_ns
from .main.views.time_views import api as timings_ns

from app.main.auth.controller.auth_controler import api as login_ns
from app.main.auth.controller.regestiter_controler import api as register_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
        title='Sokosolar documention ',
        version='1.0',
        description=' project route '
        )

api.add_namespace(products_ns, path='/product')
api.add_namespace(comments_ns, path='/comments')
api.add_namespace(timings_ns, path='/time')
api.add_namespace(login_ns, path='/auth')
api.add_namespace(register_ns, path='/user')

