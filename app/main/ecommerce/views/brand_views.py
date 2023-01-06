from flask                     import request
from flask_restx               import Resource
from app.main.ecommerce.model.submodel   import Brand
from app.main.ecommerce.schema.schema    import BrandSchema
from app.main.ecommerce.utils.dto        import BrandDto
from ....main                       import db
from app.main.auth.models.user      import User
from app.main.auth.extensions.auth.api_doc_required import permission




api              = BrandDto.api
_brand           = BrandDto.brand
item_schema      = BrandSchema()
item_list_schema = BrandSchema(many=True)



@api.route("/")
class BrandList(Resource):
    @permission
    @api.doc('List of brands')
    @api.marshal_list_with(_brand  , envelope='data')
    def get(self):
        return item_list_schema.dump(Brand.find_all()), 200


    @permission
    @api.response(201, 'Brand name added successfully')
    @api.doc("Adding Brand name")
    @api.expect(_brand , validate=True)
    def post(self):
        item_json         = request.get_json()
        nameConfirmation  = Brand.query.filter_by(name=item_json["name"]).first()
        author            = User.query.filter_by(id=item_json['author']).first()

        if author:
            if not nameConfirmation:
                item_data = item_schema.load(item_json)
                db.session.add(item_data)
                db.session.commit()
                return item_schema.dump(item_data), 201
                    
            else:
                return {"message": "Name already exist"}, 201
        else:
            return {"message": "Invalid user ID"}, 404


@api.route('/<int:id>')
class BrandFilter(Resource):
    @permission
    @api.doc('deleting brand name')
    @api.marshal_with(_brand)
    def delete(self, id):
        item_data = Brand.query.filter_by(id=id).first()
        if not item_data:
            return{"message":"Item is not found"}
        else:
            db.session.delete(item_data)
            db.session.commit()
            return {"message":"deleted successfully"}


    @permission
    @api.doc("get brand name by id")
    @api.marshal_with(_brand)
    def get(self, id):
        item_data = Brand.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        return item_schema.dump(item_data), 200

        
    @permission
    @api.doc('edit brand name')
    @api.marshal_with(_brand)
    @api.expect(_brand, validate=True)
    def put(self, id):
        item_data = Brand.query.filter_by(id=id).first_or_404(description=f" not found in database.")
        item_json = request.get_json()
      
        if item_data:
            item_data.name=item_json['name']
           
            db.session.add(item_data)
            db.session.commit()
        return  item_schema.dump(item_data), 200

@api.route('/user/<int:userId>')
@api.param('UserId', 'The User identifier')
class FilterBrand(Resource):
    @permission
    @api.doc('Getting solar brand posted by specific user')
    @api.marshal_list_with(_brand, envelope='data')
    def get(self, userId):
        brand = Brand.query.filter_by(author=userId).all()
        if brand:
            return item_list_schema.dump(brand), 201
        else:
            return {
                "message": "You haven't uploaded any Product brand yet"
            }, 401




