from backend import create_app
from flask import request, jsonify, Response

app = create_app()

if __name__ =="__main__":
    app.run(host="0.0.0.0", debug=True)