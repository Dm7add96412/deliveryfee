from flask import Blueprint, jsonify, Response, request
from datetime import datetime

api_bp = Blueprint("api", __name__, url_prefix="/api")

def calc_value(value: int):
    if value < 1000:
        return 1000 - value
    else:
        return 0

def calc_items(items: int):
    i = 5
    fee = 0
    if items < i:
        return 0
    if items > 12:
        fee = 120
    while i < items:
        i += 1
        fee += 50
    fee += 50
    return fee

def calc_distance(distance: int):
    i = 1000
    fee = 200
    if distance <= i:
        return fee
    while i <  distance:
        i += 500
        fee += 100
    return fee

def check_time(time: str):
    timeobject = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    weekday = timeobject.isoweekday()
    min_time = datetime(2023, 1, 1, 15)
    max_time = datetime(2023, 1, 1, 19)
    if weekday != 5:
        return 1
    if timeobject.time() >= min_time.time() and timeobject.time() <= max_time.time():
        return 1.2
    return 1

@api_bp.route('/delivery-price', methods=['POST'])
def delivery_price():
    content = request.json

    cart_value = content['cart_value']
    delivery_distance = content['delivery_distance']
    number_of_items = content['number_of_items']
    timeISO = content['time']

    if cart_value >= 10000:
        return jsonify({'delivery fee': 0})

    cart = calc_value(cart_value)
    items = calc_items(number_of_items)
    distance = calc_distance(delivery_distance)
    time = check_time(timeISO)

    total = (cart + items + distance) * time
    rounded = int(total)

    if rounded > 1500:
        d_fee = 1500
    else:
        d_fee = rounded

#    print(type(time), type(number_of_items), type(delivery_distance), type(cart_value))
 #   return jsonify({'cart value': cart, 'items fee': items, 'distance fee': distance, 'time fee': time, 'rounded': rounded, 'FINAL': d_fee}), 201
#   return Response(status=204)
    return jsonify({'delivery_fee': d_fee})