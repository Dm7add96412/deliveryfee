from flask import jsonify

def calculate_fee(content):
    cart_value = content['cart_value']
    delivery_distance = content['delivery_distance']
    number_of_items = content['number_of_items']
    time = content['time']

    return jsonify({'result': 'success!'})