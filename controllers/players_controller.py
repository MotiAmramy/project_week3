from flask import Blueprint, request, jsonify

from repository.player_repository import get_players_by_positionn

players_bluprint = Blueprint("player", __name__)

@players_bluprint.route('/s', methods=['GET'])
def get_all():
    # year = request.args.get("year")
    # position = request.args.get("position")
    # alll = get_players_by_positionn(year, position)
    return "jsonify(alll)", 200