from api.api_request import get_api_players
from models.Player import Player
from models.Season import Season
from repository.player_repository import create_player
from repository.season_repository import create_season


def convert_to_season(json,p_id):
    new_season =  Season(player_id=p_id,position=json["position"],
                  games_started=json["gamesStarted"],games=json["games"],
                    age=json["age"],two_fg=json["twoFg"],
                    three_percent=json["threePercent"],three_attempts=json["threeAttempts"],
                    three_fg=json["threeFg"],field_percent=json["fieldPercent"],
                    field_attempts=json["fieldAttempts"],field_goals=json["fieldGoals"],
                    minutes_pg=json["minutesPg"],total_rb=json["totalRb"],
                    defensive_rb=json["defensiveRb"],offensive_rb=json["offensiveRb"],
                  ft_percent=json["ftPercent"],ft_attempts=json["ftAttempts"],
                    ft=json["ft"],effective_fg_percent=json["effectFgPercent"],
                    two_percent=json["twoPercent"],two_attempts=json["twoAttempts"],
                    season=json["season"],team=json["team"],
                  points=json["points"],personal_fouls=json["personalFouls"],
                  turnovers=json["turnovers"],blocks=json["blocks"],
                    steals=json["steals"],assists=json["assists"]
                  )
    create_season(new_season)



def convert_to_player(data):
    new_player = Player(
        position=data.get("position"),
        name=data.get("playerName")
    )
    p_id = create_player(new_player)
    return p_id





