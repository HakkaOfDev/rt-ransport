from flask import jsonify, Blueprint, request, abort, Response

from data.User import User
from encoders.UserEncoder import UserEncoder
from services.UserService import UserService
from tools.Keys import URL_USER
import json

userService = UserService()
users_bp = Blueprint('users_bp', __name__)


@users_bp.route(URL_USER + 'all', methods=['GET'])
def getAllUsers():
    users = userService.findAll()
    response = []
    for user in users:
        response.append(json.loads(json.dumps(user, indent=4, cls=UserEncoder)))
    return jsonify(response)


@users_bp.route(URL_USER + 'register', methods=['POST'])
def registerNewUser():
    data = request.get_json()
    user = User(data['first_name'], data['last_name'], data['email'], data['password'], data['address'],
                data['tel'], data['admin'])
    if not userService.ifUserExists(user):
        userService.registerNewUser(user)
        abort(Response('Registration successful', status=200, mimetype='application/json'))
    else:
        abort(Response('User already exists', status=400, mimetype='application/json'))


@users_bp.route(URL_USER + 'login', methods=['POST'])
def loginUser():
    data = request.get_json()
    email = data['email']
    password = data['password']
    if userService.ifUserExistsWithEmail(email):
        if userService.loginUser(email, password):
            abort(Response('Login successful', status=200, mimetype='application/json'))
        else:
            abort(Response('Invalid credentials', status=400, mimetype='application/json'))
    else:
        abort(Response('User doesn\'t exists', status=400, mimetype='application/json'))
