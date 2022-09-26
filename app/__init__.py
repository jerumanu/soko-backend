from flask_restx import Api
from flask import Blueprint



blueprint = Blueprint('api', __name__)

api = Api(blueprint,
        title='Sokosolar documentaion ',
        version='1.0',
        description=' project route '
        )