from crypt import methods
from flask import Flask, Blueprint, jsonify, make_response
from flask_restx  import Resource, Api

home = Blueprint('home', __name__)

api = Api(home,
        title='Sokosolar documention ',
        version='1.0',
        description=' project route '
        
        )

@api.route('/', methods=['GET', 'POST'])
class HelloWorld(Resource):
    def get(self):
        response = { "message": "Go to /app to get all the endpoints"}
        return make_response(jsonify(response))
