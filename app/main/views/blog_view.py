from flask                          import request
from flask_restx                    import Resource
from app.main.model.blog_model      import BlogModel
from app.main.schema.schema         import BlogSchema
from app.main.utils.dto             import BlogDto
from ..                             import db


api              = BlogDto.api
_blog            = BlogDto.blog
item_schema      = BlogSchema()
item_list_schema = BlogSchema(many=True)


@api.route("/")
class Blog(Resource):
    @api.doc('List of frequently asked questions')
    @api.marshal_list_with(_blog , envelope='data')
    def get(self):
        return item_list_schema.dump(BlogModel.find_all()), 200

    @api.response(201, 'FAQ added successfully')
    @api.doc("Adding FAQ")
    @api.expect(_blog , validate=True)
    def post(self):
        item_json         = request.get_json()
        titleConfirmation = BlogModel.query.filter_by(title=item_json["title"]).first()

        if not titleConfirmation:
            item_data = item_schema.load(item_json)
            db.session.add(item_data)
            db.session.commit()
            return item_schema.dump(item_data), 201
                
        else:
            return {"message": "Title already exist"}, 201


@api.route('/<int:id>')
class Blog(Resource):
    @api.doc('deleting FAQ')
    @api.marshal_with(_blog )
    def delete(self, id):
        item_data = BlogModel.query.filter_by(id=id).first()
        if not item_data:
            return{"message":"Item is not found"}
        else:
            db.session.delete(item_data)
            db.session.commit()
            return {"deleted successfully"}

    
    @api.doc("get category by id")
    @api.marshal_with(_blog )
    def get(self, id):
        item_data = BlogModel.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        return item_schema.dump(item_data), 200

        

    @api.doc('edit Frequently asked questions')
    @api.marshal_with(_blog )
    @api.expect(_blog, validate=True)
    def put(self, id):
        item_data = BlogModel.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        item_json = request.get_json()
        print("hello", item_data)
        print("world", item_json)
        if item_data:
            item_data.title=item_json['title']
            item_data.description=item_json['description']
            
        else:
            item_data = item_schema.load(item_json)

        db.session.add(item_data)
        db.session.commit()
        return  item_schema.dump(item_data), 200



