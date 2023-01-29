from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

# route for error messages with custom error messages

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(NotFound)
def generic_exception(err):
    return jsonify({"message": "Cannot be found"}), 404

@error_bp.app_errorhandler(ValueError)
def generic_exception(err):
    return jsonify({"message": "An attribute value is not correct in request data"}), 500

@error_bp.app_errorhandler(KeyError)
def generic_exception(err):
    return jsonify({"message": "A keyerror has occured in request data"}), 500

@error_bp.app_errorhandler(Exception)
def generic_exception(err):
    return jsonify({"message": "An error has occured"}), 500