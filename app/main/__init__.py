from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt     import Bcrypt
from flask_mail       import Mail
from flask_cors       import CORS
from .config          import config_by_name
from flask_bcrypt     import Bcrypt
from flask_mail       import Mail
from flask_mpesa      import MpesaAPI
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

# from flask_login import LoginManager
# z
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
mail= Mail()
cors= CORS()
mpesa_api=MpesaAPI()

# login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['MAIL_SERVER']         = 'smtp.gmail.com'
    app.config['MAIL_SERVER']         = 'smtp.gmail.com'
    app.config['MAIL_PORT']           = 465
    app.config['MAIL_USERNAME']       = 'mwasjopa@gmail.com'
    app.config['MAIL_PASSWORD']       = 'nxufknsrfdsvsajh'
    app.config['MAIL_DEFAULT_SENDER'] = 'mwasjopa@gmail.com'
    app.config['MAIL_MAX_EMAILS ']    = None
    app.config['MAIL_USE_TLS']        = False
    app.config['MAIL_USE_SSL']        = True
    app.config["API_ENVIRONMENT"]     = "sandbox" #sandbox or production
    app.config["APP_KEY"]             = "vbxsneeZ9IMFoyKKIgOIQQZFlawAADnP" # App_key from developers portal
    app.config["APP_SECRET"]          = "WAzDhQVhitIXwiTc" #App_Secret from developers portal
    cors.init_app(app)
    mail.init_app(app)
    mpesa_api.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)
    flask_bcrypt.init_app(app)
    

    return app

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))