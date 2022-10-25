from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_cors import CORS

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
mail= Mail()
cors= CORS()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['MAIL_SERVER']         = 'smtp.gmail.com'
    app.config['MAIL_PORT']           = 465
    app.config['MAIL_USERNAME']       = 'mwasjopa@gmail.com'
    app.config['MAIL_PASSWORD']       = 'nxufknsrfdsvsajh'
    app.config['MAIL_DEFAULT_SENDER'] = 'mwasjopa@gmail.com'
    app.config['MAIL_MAX_EMAILS ']    = None
    app.config['MAIL_USE_TLS']        = False
    app.config['MAIL_USE_SSL']        = True
    mail.init_app(app)
    cors.init_app(app, origins=["*", "http://localhost:3000"], supports_credentials = True)
    db.init_app(app)
    flask_bcrypt.init_app(app)
    mail.init_app(app)

    return app