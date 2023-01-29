from flask import Blueprint, jsonify

# a route for a simple health check of the server

health_bp = Blueprint("health", __name__)

@health_bp.route('/health', methods=['GET'])
def hello():
    l = {'info': 'server is running'}
    return jsonify(l), 200
