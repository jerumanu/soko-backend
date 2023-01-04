from flask                          import  request
from flask_restx                    import  Resource
from app.main.ecommerce.model.favourite_model import  FavouriteModel
from app.main.ecommerce.schema.schema         import  FavouriteSchema
from app.main.ecommerce.utils.dto             import  FavouriteDto
from  ....main import db
from app.main.ecommerce.model.product_model   import  ProductModel
from app.main.auth.models.user      import  User

api              = FavouriteDto.api
_favourite       = FavouriteDto.favourite
item_schema      = FavouriteSchema()
item_list_schema = FavouriteSchema(many=True)




@api.route('/<int:id>')
class Favourite(Resource):
    @api.doc('add specific product as favourite and getting specific product add as favourite by specific user')
    @api.marshal_with(_favourite)
    def delete(self, id):
        favourite = FavouriteModel.find_by_id(id)
        if not favourite:
            return{"message":"Item is not found"}, 404
        else:
            db.session.delete(favourite)
            db.session.commit()
            return {"item removed successfully"}, 201


@api.route('/')
class Favourite(Resource):
    @api.doc('geting all favourite product for specific user')
    @api.marshal_list_with(_favourite, envelope='favourite')
    def get(self):
        return item_list_schema.dump(FavouriteModel.find_all()), 200

    
    
    
    
    
    @api.response(201, 'Saved successfully')
    @api.doc("Adding Save")
    @api.expect(_favourite, validate=True)
    def post(self):
        item_json  = request.get_json()
        product    = ProductModel.query.filter_by(id=item_json['product_id']).first_or_404(description=f"no product found")
        author     = User.query.filter_by(id=item_json['user_id']).first()
        
        if author:
            if product:
                favourite_item = item_schema.load(item_json)
                db.session.add(favourite_item)
                db.session.commit()
                return item_schema.dump(favourite_item), 201
            else:
                return {"message": ""}
        else:
            return{"message": "Invalid user Id"}
    
