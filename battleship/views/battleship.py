from http import HTTPStatus
from flask import jsonify, Blueprint, request
from ..models.battleship import Battleship
from ..api import db
from ..serializers.battleship import BattleshipSchema

ship = Blueprint('ship', __name__)


@ship.route('/battleship', methods=['POST'])
def create_battleship_game():
    loader = BattleshipSchema().load(request.get_json())
    obj = Battleship(**loader)
    db.session.add(obj)
    db.session.commit()
    return jsonify(BattleshipSchema().dump(obj)), 201


@ship.route('/battleship', methods=['PUT'])
def shot():
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED


@ship.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED
