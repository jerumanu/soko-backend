from flask.json import jsonify
from app.main import db
from app.main.ecommerce.model.star_rating import StarRatingModel
from flask                        import request
from flask                                       import Blueprint


rate = Blueprint('rate', __name__ ,url_prefix="/rate" )

@rate.route('/', methods=['POST', 'GET'])
def rating():
    

    if request.method == 'POST':

        five_stars = request.get_json().get('five_stars', '')
        four_stars = request.get_json().get('four_stars', '')
        three_stars = request.get_json().get('three_stars', '')
        two_stars = request.get_json().get('two_stars', '')
        one_star = request.get_json().get('one_stars', '')
        count =request.get_json().get('count', '')
        rating =request.get_json().get('rating', '')
        total = request.get_json().get('total', '')
        
        content = 0

        if content :
                    
                if content==5:
                    five_stars += 1
                elif content==4:
                    four_stars += 1
                elif content == 3:
                    three_stars += 1
                elif content == 2 :
                    two_stars += 1

                elif content ==1:
                    one_star +=1
                count +=1
                total += content

                rating=float("{0:.1f}" .format(total/count))
        rate =StarRatingModel(five_stars=five_stars, 
        four_stars=four_stars, 
        three_stars=three_stars,
        two_stars=two_stars,
        one_star=one_star,
        count=count,
        rating =rating,
        total= total
        )
        db.session.add(rate)
        db.session.commit()

        return jsonify({
            
            'five_stars':rate.five_stars ,
            'four_stars': rate.four_stars,
            'three_stars':rate.three_stars,
            'two_stars': rate.two_stars,
            'one_star': rate.one_star,
            'count':rate.count ,
            'rating':rate.rating,
            'total':rate.total
        }), 201
    else:

        # page = request.args.get('page', 1, type=int)
        # per_page = request.args.get('per_page', 5, type=int)

        rate = StarRatingModel.query.all()

        data = []

        for rate in rate:
            data.append({
            'id': rate.id,
            'five_stars':rate.five_stars ,
            'four_stars': rate.four_stars,
            'three_stars':rate.three_stars,
            'two_stars': rate.two_stars,
            'one_star': rate.one_star,
            'count':rate.count ,
            'rating':rate.rating,
            'total':rate.total
            })
        # meta = {
        #      'id': rate.id,
        #     'five_stars':rate.five_stars ,
        #     'four_stars': rate.four_stars,
        #     'three_stars':rate.three_stars,
        #     'two_stars': rate.two_stars,
        #     'one_star': rate.one_star,
        #     'count':rate.count ,
        #     'rating':rate.rating,
        #     'total':rate.total

        # }

        return jsonify({'data': data, }), 200

        
