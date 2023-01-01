from flask_restx                                  import Api, Resource
from flask                                        import Blueprint
from .main.ecommerce.views.payments_view          import api as payment_ns
from .main.ecommerce.views.products_views         import api as products_ns
from .main.ecommerce.views.subscribe_views        import api as subscribe_ns
from .main.ecommerce.views.category_views         import api as category_ns
from .main.ecommerce.views.faq_views              import api as faq_ns
from .main.ecommerce.views.blog_view              import api as blog_ns
from .main.ecommerce.views.favourite_views        import api as favourite_ns
from .main.ecommerce.views.comment_views          import api as comments_ns
from .main.ecommerce.views.time_views             import api as timings_ns
from app.main.auth.controller.auth_controler      import api as login_ns
from app.main.auth.controller.register_controler  import api as register_ns
from app.main.auth.controller.user_controler      import api as users_ns
from .main.ecommerce.views.Star_rating            import api as rating_ns
from .main.qoutation.views.dereted_power          import api as dereted_ns
from .main.qoutation.views.load_analysis          import api as load_ns
from  .main.qoutation.views.batt_views            import api as batt_ns
from  .main.auth.views.engineer_views             import api as engineer_ns
from  .main.auth.views.business_views             import api as business_ns
from .main.ecommerce.views.brand_views            import api as brand_ns
from .main.ecommerce.views.solarType_views        import api as solarType_ns
from .main.qoutation.views.qoute_views            import api as qoute_ns
from  . main.qoutation.views.inverter_views       import api as inverter_ns
from .main.qoutation.views.voltsdropdown          import api as voltsdrop_ns

# blueprint = Blueprint('api', __name__ , )


blueprint = Blueprint('api', __name__, url_prefix="/app")

api = Api(blueprint,
        title='Sokosolar documention ',
        version='1.0',
        description=' project route '
        
        )



api.add_namespace(products_ns,  path='/product')
api.add_namespace(payment_ns,   path='/payment')
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
api.add_namespace(rating_ns,    path='/ratings')
api.add_namespace(dereted_ns,   path="/dereted")
api.add_namespace(load_ns,      path="/analysis")
api.add_namespace(batt_ns,      path="/batt")
api.add_namespace (engineer_ns, path="/engineer")
api.add_namespace (business_ns, path='/business')
api.add_namespace (users_ns,    path='/userList')
api.add_namespace(brand_ns,     path='/brand')
api.add_namespace(solarType_ns, path='/solar-type')

api.add_namespace(qoute_ns ,    path='/qoute')
api.add_namespace(inverter_ns , path='/inverter')
api.add_namespace(voltsdrop_ns, path='/voltsdrop')


