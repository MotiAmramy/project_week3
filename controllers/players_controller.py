from flask import Blueprint, request, jsonify
from repository.player_repository import get_players_by_positionn

players_bluprint = Blueprint("player", __name__)

@players_bluprint.route('/', methods=['GET'])
def get_all():
    year = request.args.get("year")
    position = request.args.get("position")
    all_players = get_players_by_positionn(year, position)
    return jsonify(all_players), 200






