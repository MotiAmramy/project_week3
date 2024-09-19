from flask import Flask, request, jsonify
from repository.player_repository import get_players_by_positionn



app = Flask(__name__)



@app.route('/api/players?position={position}&season={season}?', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season', None)
    list_of_players = get_players_by_positionn(season, position)
    jsonify(list_of_players), 200




a = get_players_by_positionn(2024, "SG")



if __name__ == '__main__':
    app.run(debug=True)

