from flask import Flask, request, jsonify
from repository.player_repository import get_players_by_positionn
from controllers.players_controller import players_bluprint



app = Flask(__name__)
app.register_blueprint(players_bluprint, url_prefix="/api/players")

if __name__ == '__main__':
    alll = get_players_by_positionn(2024, "SG")
    print(alll)
    app.run(debug=True)