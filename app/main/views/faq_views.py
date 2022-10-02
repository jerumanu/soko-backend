from wsgiref import validate
from flask                          import request
from flask_restx                    import Resource
from app.main.model.faq_model       import FaqModel
from app.main.schema.schema         import FaqSchema
from app.main.utils.dto             import FaqDto
from ..                             import db


api              = FaqDto.api
_faq        = FaqDto.category
item_schema      = FaqSchema()
item_list_schema = FaqSchema(many=True)


@api.route("/")
class Faq(Resource):
    @api.doc('List of frequently asked questions')
    @api.marshal_list_with(_faq, envelope='data')
    def get(self):
        return item_list_schema.dump(FaqModel.find_all()), 200

    @api.response(201, 'FAQ added successfully')
    @api.doc("Adding FAQ")
    @api.expect(_faq, validate=True)
    def post(self):
        item_json         = request.get_json()
        titleConfirmation = FaqModel.query.filter_by(title=item_json["title"]).first()

        if not titleConfirmation:
            item_data = item_schema.load(item_json)
            db.session.add(item_data)
            db.session.commit()
            return item_schema.dump(item_data), 201
                
        else:
            return {"message": "Title already exist"}, 201


@api.route('/<int:id>')
class Faq(Resource):
    @api.doc('deleting FAQ')
    @api.marshal_with(_faq)
    def delete(self, id):
        item_data = FaqModel.query.filter_by(id=id).first()
        if not item_data:
            return{"message":"Item is not found"}
        else:
            db.session.delete(item_data)
            db.session.commit()
            return {"deleted successfully"}

    
    @api.doc("get category by id")
    @api.marshal_with(_faq)
    def get(self, id):
        item_data = FaqModel.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        return item_schema.dump(item_data), 200

    @api.doc('edit Frequently asked questions')
    @api.marshal_with(_faq)
    @api.expect(_faq, validate=True)
    def put(self, id):
        item_data = FaqModel.query.filter_by(id=id).first_or_404(description=f" not found in database.")
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



