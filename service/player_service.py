from api.api_request import get_api_players
from models.Player import Player
from models.Season import Season
from repository.player_repository import create_player
from repository.season_repository import create_season


def convert_to_season(data, id):
    new_season = Season(
        player_id=id,
        position=data.get("position"),
        age=data.get("age"),
        games=data.get("games"),
        games_started=data.get("gamesStarted"),
        minutes_pg=data.get("minutesPg"),
        field_goals=data.get("fieldGoals"),
        field_attempts=data.get("fieldAttempts"),
        field_percent=data.get("fieldPercent"),
        three_fg=data.get("threeFg"),
        three_attempts=data.get("threeAttempts"),
        three_percent=data.get("threePercent"),
        two_fg=data.get("twoFg"),
        two_attempts=data.get("twoAttempts"),
        two_percent=data.get("twoPercent"),
        effective_fg_percent=data.get("effectFgPercent"),
        ft=data.get("ft"),
        ft_attempts=data.get("ftAttempts"),
        ft_percent=data.get("ftPercent"),
        offensive_rb=data.get("offensiveRb"),
        defensive_rb=data.get("defensiveRb"),
        total_rb=data.get("totalRb"),
        assists=data.get("assists"),
        steals=data.get("steals"),
        blocks=data.get("blocks"),
        turnovers=data.get("turnovers"),
        personal_fouls=data.get("personalFouls"),
        points=data.get("points"),
        team=data.get("team"),
        season=data.get("season")
    )
    create_season(new_season)



def convert_to_player(data):
    new_player = Player(
        position=data.get("position"),
        name=data.get("playerName")
    )
    p_id = create_player(new_player)
    return p_id





