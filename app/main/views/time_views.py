from app.main import db
from app.main.model.timming_model import  TimeFormat

from flask import request
from flask_restx import Resource



# from ..schema.schema import  TimeSchema



from ..utils.dto import TimeDto

api = TimeDto.api
_timings = TimeDto.timings

COMMENT_NOT_FOUND = "Comment not found."

# time_schema=  TimeSchema()
# time_list_schema = TimeSchema( many=True)

@api.route('/<int:id>')
@api.param('comment_id', 'The User identifier')
class Comments(Resource):
    @api.doc('get a product')
    @api.marshal_with(_timings)


    def delete(self,id):
        comment_data = TimeFormat.find_by_id(id)
        if comment_data:
            comment_data.delete_from_db()
            return {'message': "comments Deleted successfully"}, 200
        return {'message': COMMENT_NOT_FOUND}, 404

   
    @api.doc('delete a product')
    @api.marshal_with(_timings)

    def put(self, id):
        comment_data = TimeFormat.find_by_id(id)
        comment_json = request.get_json();

        if comment_data:
            comment_data.comment= comment_json['comment']
            
        else:
            comment_data = time_schema.load(comment_json)

        comment_data.save_to_db()
        return time_schema.dump(comment_data), 200

@api.route('/')
class CommentsList(Resource):
   
    @api.doc('list_of_timings')
    @api.marshal_list_with(_timings, envelope='data')
    def get(self):
        return time_list_schema.dump(TimeFormat.find_all()), 200

    

    @api.response(201, 'comment successfully created.')
    @api.doc('create a new comment')
    @api.expect(_timings, validate=True)
    def post(self):
        comment_json = request.get_json()
        comment_data = time_schema.load(comment_json)
        comment_data.save_to_db()

        return time_schema.dump(comment_data), 201