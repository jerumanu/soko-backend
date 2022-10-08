from app.main import db
from app.main.model.comment_model import CommentsModel

from flask import request
from flask_restx import Resource



from ..schema.schema import  CommentsSchema



from ..utils.dto import CommentsDto

api = CommentsDto.api
_comments = CommentsDto.comments

COMMENT_NOT_FOUND = "Comment not found."

comments_schema=  CommentsSchema()
comments_list_schema = CommentsSchema( many=True)

@api.route('/<int:id>')
@api.param('comment_id', 'The User identifier')
class Comments(Resource):
    @api.doc('get a product')
    @api.marshal_with(_comments)

    def get(self, id):
        comment_data = CommentsModel.find_by_id(id)
        if comment_data:
            return comments_schema.dump(comment_data)
        return {'message': COMMENT_NOT_FOUND}, 404
    @api.doc('delete  a product')
    @api.marshal_with(_comments)

    def delete(self,id):
        comment_data = CommentsModel.find_by_id(id)
        if comment_data:
            comment_data.delete_from_db()
            return {'message': "comments Deleted successfully"}, 200
        return {'message': COMMENT_NOT_FOUND}, 404

   
    @api.doc('delete a product')
    @api.marshal_with(_comments)

    def put(self, id):
        comment_data = CommentsModel.find_by_id(id)
        comment_json = request.get_json();

        if comment_data:
            comment_data.comment= comment_json['comment']
            
        else:
            comment_data = comments_schema.load(comment_json)

        comment_data.save_to_db()
        return comments_schema.dump(comment_data), 200

@api.route('/')
class CommentsList(Resource):
   
    @api.doc('list_of_comments')
    @api.marshal_list_with(_comments, envelope='data')
    def get(self):
        return comments_list_schema.dump(CommentsModel.find_all()), 200

    

    @api.response(201, 'comment successfully created.')
    @api.doc('create a new comment')
    @api.expect(_comments, validate=True)
    def post(self):
        comment_json = request.get_json()
        comment_data = comments_schema.load(comment_json)
        comment_data.save_to_db()

        return comments_schema.dump(comment_data), 201