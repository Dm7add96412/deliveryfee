from flask import Blueprint, jsonify, request
from backend.modules import datavalidation, datacalculations

# route for POST request for calculating and returning delivery fee

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route('/delivery-price', methods=['POST'])
def delivery_price():
# check that data is in JSON format
    if request.is_json:
        print("Data in JSON format")
    else:
        return jsonify({"message": "Data not in JSON format"}), 400
    content = request.json

# check that data in needed format for calculations
    data_check = datavalidation.DataValidator(content)
    checked_data = data_check.validate_data()

# delivery calculations
    # if cart value is equal or more than 100€ delivery fee of 0€ will be returned
    if content['cart_value'] >= 10000:
        return jsonify({'delivery fee': 0}), 200

    cart_data = datacalculations.DataCalculator(content)
    cart_fee = cart_data.calc_cartfee()
    distance_fee = cart_data.calc_distance()
    items_fee = cart_data.calc_items()
    time_fee = cart_data.check_time()

    total = (cart_fee + items_fee + distance_fee) * time_fee
    rounded = int(total)

    if rounded > 1500:
        d_fee = 1500
    else:
        d_fee = rounded

    return jsonify({'delivery_fee': d_fee}), 200