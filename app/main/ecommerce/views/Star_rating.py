from flask.json import jsonify
# from cgi import print_arguments
from statistics import mean
import string

from app.main import db
from app.main.ecommerce.model.star_rating import StarRatingModel
from app.main.ecommerce.schema.schema import RatingsSchema
from flask                        import request
from flask_restx                  import Resource
from app.main.ecommerce.model.product_model import ProductModel
from app.main.auth.extensions.auth.api_doc_required import permission


from ..utils.dto import StarDto
import json

api =  StarDto.api
_star=  StarDto.star


star_schema= RatingsSchema()

star_list_schema =  RatingsSchema( many=True)


@api.route('/')
class StarRating(Resource):
    @permission
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_star, validate=True)

    # refactor the code  to alow mean callculation befor the serialization 

    def post(self):
        star_json= request.get_json()

        
        productId     = ProductModel.query.filter_by(id=star_json['product_id']).first()
        

        
        if productId:
            star_ratting_data = star_schema.load(star_json)

            star_ratting_data.save_to_db()

            return star_schema.dump(star_ratting_data), 201
        else:
                return {"message": "Prodcut not found"}, 404    

@api.route('/rate')
class Starratinglist(Resource):
    @permission
    @api.doc('product ratting')
    @api.marshal_list_with(_star)
    @permission
    def get(self,product_id):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0

        start_json =  StarRatingModel.query.filter_by(product_id=product_id).all()
        
        result= star_list_schema.dump(start_json)
        

        num= mean(d['rating'] for d in result)
        # s = format(x, '.5f')
        avg =float(format(num, '.1f'))

        # print("hello world")
        print(num)
        print(result)


        data = dict()

        
        data['avg'] = avg
        print (data)
        

        return jsonify({'data':data}) 


# @api.route('/star/<int:product_id>')
# @api.param('UserId', 'The User identifier')
# class ProductFilter(Resource):
#     @api.doc('Your owner')
#     @api.marshal_with(_products)
#     def get(self, product_id):
#         start_json = ProductModel.query.filter_by(product_id=product_id).all()
#         if product_json:
#             return product_list_schema.dump(product_json)
#         return jsonify({
#             "message": "sorry no ratting yet"
#         })   
    

        
        
#         # return star_list_schema .dump( StarRatingModel.find_all()), 200
