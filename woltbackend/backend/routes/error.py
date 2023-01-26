from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(NotFound)
def generic_exception(err):
    return jsonify({"message": "Cannot be found"}), 404
 #   return err, 500

@error_bp.app_errorhandler(Exception)
def generic_exception(err):
    return jsonify({"message": "Unkown error"}), 500
 #   return err, 500
