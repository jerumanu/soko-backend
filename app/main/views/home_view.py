from crypt import methods
from flask import Flask, Blueprint, jsonify, make_response
from flask_restx  import Resource, Api

home = Blueprint('home', __name__)



@home.route('/', methods=['GET', 'POST'])
class HelloWorld(Resource):
    def get(self):
        response = {'status': 'fail', "message": "Account does not seem to exist"}
        return make_response(jsonify(response))
