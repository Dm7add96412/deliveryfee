from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route('/health', methods=['GET'])
def hello():
    l = [{'id': 1, 'info': 'some info'}, {'id': 2, 'info': 'some other info here'}]
    print(l)
    return jsonify(l)
