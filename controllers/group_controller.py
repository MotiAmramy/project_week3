from flask import Blueprint, request, jsonify

from models.Group import Group
from repository.group_repository import create_group, find_all_groups
from repository.player_repository import get_players_by_positionn, create_table_player

groups_bluprint = Blueprint("teem", __name__)



@groups_bluprint.route('/', methods=['GET'])
def get_all():
    all_teems = find_all_groups()
    return jsonify(all_teems), 200




@groups_bluprint.route('/', methods=['POST'])
def create():
    all_data = request.json
    li = all_data["player_id"]
    new_teem = Group(all_data["name"], li[0], li[1], li[2], li[3], li[4])
    create_group(new_teem)
    return "jsonify(new_teem)", 201


