from flask_restx import Api
from flask import Blueprint

from .main.views.products_views import api as products_ns
from .main.views.comment_views import api as comments_ns
from .main.views.time_views import api as timings_ns

from .main.auth.user_controler import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
        title='Sokosolar documentaion ',
        version='1.0',
        description=' project route '
        )

api.add_namespace(products_ns, path='/product')
api.add_namespace(comments_ns, path='/comments')
api.add_namespace(timings_ns, path='/time')
api.add_namespace(user_ns, path='/user')

