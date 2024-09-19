
from flask import Flask, request, jsonify

from repository.group_repository import create_table_group
from repository.player_repository import get_players_by_positionn, find_all_players, create_table_player
from controllers.players_controller import players_bluprint
from controllers.group_controller import groups_bluprint
from repository.season_repository import find_all_seasons, create_seasons_tables
from repository.seed import create_player_and_season, drop_table



app = Flask(__name__)
app.register_blueprint(players_bluprint, url_prefix="/api/players")
app.register_blueprint(groups_bluprint, url_prefix="/api/teems")


if __name__ == '__main__':
    drop_table()
    create_table_player()
    create_seasons_tables()
    create_table_group()
    create_player_and_season(2024)
    create_player_and_season(2023)
    create_player_and_season(2022)
    app.run(debug=True)