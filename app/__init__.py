from flask_restx import Api
from flask import Blueprint

from .main.views.products_views  import api as products_ns
from .main.views.subscribe_views import api as subscribe_ns
from .main.views.category_views  import api as category_ns
from .main.views.faq_views       import api as faq_ns
from .main.views.blog_view       import api as blog_ns
from .main.views.favourite_views import api as favourite_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
        title='Sokosolar documentaion ',
        version='1.0',
        description=' project route '
        )

api.add_namespace(products_ns,  path='/product')
api.add_namespace(subscribe_ns, path='/subscribe')
api.add_namespace(category_ns,  path='/category')
api.add_namespace(faq_ns,       path='/faq')
api.add_namespace(blog_ns,      path='/blog')
api.add_namespace(favourite_ns, path='/favourite')
