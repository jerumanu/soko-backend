from flask_restx                                 import Api
from flask                                       import Blueprint
from .main.views.products_views                  import api as products_ns
from .main.views.subscribe_views                 import api as subscribe_ns
from .main.views.category_views                  import api as category_ns
from .main.views.faq_views                       import api as faq_ns
from .main.views.blog_view                       import api as blog_ns
from .main.views.favourite_views                 import api as favourite_ns
from .main.views.comment_views                   import api as comments_ns
from .main.views.time_views                      import api as timings_ns
from app.main.auth.controller.auth_controler     import api as login_ns
from app.main.auth.controller.register_controler import api as register_ns
from .main.views.Star_rating                    import api as rating_ns

blueprint = Blueprint('api', __name__ ,url_prefix="/soko" )



api = Api(blueprint,
        title='Sokosolar documention ',
        version='1.0',
        description=' project route '
        
        )

api.add_namespace(products_ns,  path='/')
api.add_namespace(subscribe_ns, path='/subscribe')
api.add_namespace(category_ns,  path='/category')
api.add_namespace(faq_ns,       path='/faq')
api.add_namespace(blog_ns,      path='/blog')
api.add_namespace(favourite_ns, path='/favourite')
api.add_namespace(products_ns,  path='/product')
api.add_namespace(comments_ns,  path='/comments')
api.add_namespace(timings_ns,   path='/time')
api.add_namespace(login_ns,     path='/auth')
api.add_namespace(register_ns,  path='/user')
api.add_namespace(rating_ns,  path='/ratings')
