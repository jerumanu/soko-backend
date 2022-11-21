from flask.json import jsonify
# from cgi import print_arguments
from statistics import mean
import string
from itsdangerous import json
from app.main import db
from app.main.ecommerce.model.star_rating import StarRatingModel
from app.main.ecommerce.schema.schema import RatingsSchema
from flask                        import request
from flask_restx                  import Resource
from ..utils.dto import StarDto
import json

api =  StarDto.api
_star=  StarDto.star


star_schema= RatingsSchema()

star_list_schema =  RatingsSchema( many=True)


@api.route('/')
class StarRating(Resource):

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new Product')
    @api.expect(_star, validate=True)

    # refactor the code  to alow mean callculation befor the serialization 

    def post(self):
        star_json= request.get_json()
        # product_data = request.get_json().load()

        
        # result= star_list_schema .dump( StarRatingModel.find_all())


        # num= mean(d['rating'] for d in result)

        # avg =float(format(num, '.1f'))
        # star_json['rate']=avg

        product_data=star_schema.load(star_json)
        # print(product_data)
        
        product_data.save_to_db()

        return star_schema.dump(product_data), 201

    @api.doc('list_of_products')
    # @api.marshal_list_with(_star, envelope='data')
    def get(self):
        # critic_avg = db.session.query(func.avg(Rating.rating)).scalar() or 0
        # result= star_list_schema .dump( StarRatingModel.find_all())
        

        # num= mean(d['rating'] for d in result)
        # # s = format(x, '.5f')
        # avg =float(format(num, '.1f'))
 
        # print("hello world")
        # print(num)
        # print(result)


        # data = dict()

        
        # data['avg'] = avg
        # print (data)
        
       
        # return jsonify({'data':data}) 

        
        
        return star_list_schema .dump( StarRatingModel.find_all()), 200
