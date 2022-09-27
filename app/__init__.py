from flask_restx import Api
from flask import Blueprint

from .main.views.products_views import api as products_ns
from .main.views.comment_views import api as comments_ns
blueprint = Blueprint('api', __name__)

api = Api(blueprint,
        title='Sokosolar documentaion ',
        version='1.0',
        description=' project route '
        )

api.add_namespace(products_ns, path='/product')
api.add_namespace(comments_ns, path='/comments')