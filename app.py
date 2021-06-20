from module import register, login

from functools import wraps

from flask import Flask
from flask import request
from flask import jsonify

from flask_cors import cross_origin
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def check_register_param_complete(f):
    @wraps(f)
    def is_complete(*args, **kwargs):
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        name = request.json.get('name', None)
        if email:
            if password:
                if name:
                    return f(*args, **kwargs)
                return jsonify({
                    'messages': 'missing "name" param'
                }), 400
            return jsonify({
                'messages': 'missing "password" param'
            }), 400
        return jsonify({
            'message': 'missing "email" param'
        }), 400

    return is_complete


@app.route('/api/v1/register', methods=['POST'])
@check_register_param_complete
@cross_origin()
def register_api():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    name = request.json.get('name', None)
    return register.register_data(email, password, name)
    

@app.route('/api/v1/login', methods=['GET'])
@check_register_param_complete
@cross_origin()
def login_api():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    name = request.json.get('name', None)
    return login.login_data(email, password, name)

if __name__ == '__main__':
    app.run()
