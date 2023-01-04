from flask                         import request, jsonify
from app.main                      import db
from app.main.auth.models.user     import User
from app.main.ecommerce.model.category_model import CategoryModel
from app.main.ecommerce.model.product_model  import ProductModel
from app.main.ecommerce.model.submodel import Brand, SolarType
from flask_restx                   import Resource
from ..schema.schema               import ProductSchema
from ..utils.dto                   import ProductDto
from app.main.ecommerce.model.payment_model  import Transaction
from ...decorators                  import subscription
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url



api                 = ProductDto.api
_products           = ProductDto.product
ITEM_NOT_FOUND      =  "Product Not found"
product_schema      = ProductSchema()
product_list_schema =  ProductSchema( many=True)






    
@api.route('/user/<int:userId>')
@api.param('UserId', 'The User identifier')
class ProductFilter(Resource):
    @api.doc('Your owner')
    @api.marshal_with(_products)
    def get(self, userId):
        product_json = ProductModel.query.filter_by(productOwner=userId).all()
        if product_json:
            return product_list_schema.dump(product_json)
        return jsonify({
            "message": "You haven't uploaded any Product yet"
        })      



@api.route('/<int:id>')
@api.param('id', 'The User identifier')  
class Product(Resource):
    @api.doc('delete  a product')
    @api.marshal_with(_products)
    def delete(self,id):
        product_data =  ProductModel.find_by_id(id)
        if product_data:
            product_data.delete_from_db()
            return {'message':  'Product Deleted successfully'}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, id):
        store_data = ProductModel.find_by_id(id)
        if store_data:
            return product_schema.dump(store_data)
        return {'message': ITEM_NOT_FOUND}, 404  

    


    @api.doc('delete a product')
    @api.marshal_with(_products)
    @api.expect(_products, validate=True)
    def put(self, id):
        product_data =  ProductModel.query.filter_by(id=id).first_or_404(description=f"Product not found in database.")
        product_json = request.get_json();
        category     = CategoryModel.query.filter_by(id=product_json['category_id']).first()
        solarTypeId  = SolarType.query.filter_by(id=product_json['solarType_id']).first()
        brandId      = Brand.query.filter_by(id=product_json['solarType_id']).first()

        if  product_data and category and solarTypeId and brandId:
            product_data.name = product_json['name']
            product_data.description = product_json['description']
            product_data.price = product_json['price']
            product_data.image = product_json['image']
            product_data.inStock = product_json['inStock']
            product_data.condition = product_json['condition']
            product_data.category_id = product_json['category_id']
            product_data.solarType_id = product_json['solarType_id']
            product_data.brand_id = product_json['brand_id']
            
        else:
            product_data = product_schema.load(product_json)
        product_data.save_to_db()
        return product_schema.dump(product_data), 201


@api.route('/')
class ProductList(Resource):
    @api.doc('list_of_products')
    @api.marshal_list_with(_products, envelope='data')
    def get(self):
        return product_list_schema.dump( ProductModel.find_all()), 201

      
    

    @api.response(21, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_products, validate=True)
    def post(self):
        product_json = request.get_json(force=True)
        print(product_json)
        category     = CategoryModel.query.filter_by(id=product_json['category_id']).first()
        solarTypeId  = SolarType.query.filter_by(id=product_json['solarType_id']).first()
        brandId      = Brand.query.filter_by(id=product_json['brand_id']).first()
        author       = User.query.filter_by(id=product_json["product_owner"]).first()

        if author:
            if category  and solarTypeId and brandId:
                product_data = product_schema.load(product_json)
                product_data.save_to_db()
                return {"message": "Product added successfully"}, 201
            else:
                return{"message":"The category productOwner solarType and brand is not found"}, 404
        else:
            return{"message": "Invalid user ID" }, 404
            

   
                
        
@api.route('/<name>')
@api.param('name', 'The User identifier')  
class Product(Resource):
    @api.doc('query by product name')
    @api.marshal_with(_products)
    def get(self, name):
        product_data =  ProductModel.find_by_name(name)
        if product_data:
            return product_schema.dump(product_data)
        return {'message': ITEM_NOT_FOUND}, 404  

