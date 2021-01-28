from flask import jsonify, Blueprint
from services.UserService import UserService
from tools.Keys import URL_USER
import json
from json import JSONEncoder

userService = UserService()
users_bp = Blueprint('users_bp', __name__)


@users_bp.route(URL_USER + 'all', methods=['GET'])
def getAllUsers():
    users = userService.findAll()
    response = []
    for user in users:
        response.append(json.loads(json.dumps(user, indent=4, cls=UserEncoder)))
    return jsonify(response)


class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
