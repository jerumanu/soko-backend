from wsgiref import validate
from flask                          import request
from flask_restx                    import Resource
from app.main.model.category_model  import CategoryModel
from app.main.schema.schema         import CategorySchema
from app.main.utils.dto             import CategoryDto
from ..                             import db


api              = CategoryDto.api
_category        = CategoryDto.category
item_schema      = CategorySchema()
item_list_schema = CategorySchema(many=True)


@api.route("/")
class Category(Resource):
    @api.doc('List of category names')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        return item_list_schema.dump(CategoryModel.find_all()), 200

    @api.response(201, 'Category added successfully')
    @api.doc("Adding category")
    @api.expect(_category, validate=True)
    def post(self):
        item_json = request.get_json()
        nameConfirmation = CategoryModel.query.filter_by(name=item_json["name"]).first()

        if not nameConfirmation:
            item_data = item_schema.load(item_json)
            db.session.add(item_data)
            db.session.commit()
            return item_schema.dump(item_data), 201
                
        else:
            return {"message": "The category name already exist"}, 201


@api.route('/<int:id>')
class Category(Resource):
    @api.doc('deleting category')
    @api.marshal_with(_category)
    def delete(self, id):
        item_data = CategoryModel.query.filter_by(id=id).first()
        if not item_data:
            return{"message":"Item is not found"}
        else:
            db.session.delete(item_data)
            db.session.commit()
            return {"deleted successfully"}

    
    @api.doc("get category by id")
    @api.marshal_with(_category)
    def get(self, id):
        item_data = CategoryModel.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        return item_schema.dump(item_data), 200

    @api.doc('edit category name')
    @api.marshal_with(_category)
    @api.expect(_category, validate=True)
    def put(self, id):
        item_data = CategoryModel.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        item_json = request.get_json()
        # print("hello", item_json)
        if item_data:
            item_data.name = item_json['name']
        else:
            item_data = item_schema.load(item_json)

        db.session.add(item_data)
        db.session.commit()
        return  item_schema.dump(item_data), 200

