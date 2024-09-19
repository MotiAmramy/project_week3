from models.Season import Season
from repository.database import get_db_connection
from  typing import List, Optional

def create_table_season():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasons (
    id SERIAL PRIMARY KEY,
    player_id INT NOT NULL,
    position VARCHAR(50),
    age INT,
    games INT,
    games_started INT,
    minutes_pg FLOAT,
    field_goals INT,
    field_attempts INT,
    field_percent FLOAT,
    three_fg INT,
    three_attempts INT,
    three_percent FLOAT,
    two_fg INT,
    two_attempts INT,
    two_percent FLOAT,
    effective_fg_percent FLOAT,
    ft INT,
    ft_attempts INT,
    ft_percent FLOAT,
    offensive_rb INT,
    defensive_rb INT,
    total_rb INT,
    assists INT,
    steals INT,
    blocks INT,
    turnovers INT,
    personal_fouls INT,
    points INT,
    team VARCHAR(100),
    season INT,
    FOREIGN KEY (player_id) REFERENCES players(id)
)''')


def create_season(season: Season, id : int) -> int:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO seasons (player_id, position, age, games, games_started,
                minutes_pg, field_goals, field_attempts, field_percent, three_fg,
                three_attempts, three_percent, two_fg, two_attempts, two_percent,
                effective_fg_percent, ft, ft_attempts, ft_percent,
                offensive_rb, defensive_rb, total_rb, assists, steals,
                blocks, turnovers, personal_fouls, points, team, season)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s) RETURNING id
            """, (
                id, season.position, season.age, season.games,
                season.games_started, season.minutes_pg, season.field_goals,
                season.field_attempts, season.field_percent, season.three_fg,
                season.three_attempts, season.three_percent, season.two_fg,
                season.two_attempts, season.two_percent, season.effective_fg_percent,
                season.ft, season.ft_attempts, season.ft_percent,
                season.offensive_rb, season.defensive_rb, season.total_rb,
                season.assists, season.steals, season.blocks,
                season.turnovers, season.personal_fouls, season.points,
                season.team, season.season
            ))
            new_id = cursor.fetchone()['id']  # Fetch the new season's ID
            connection.commit()
            return new_id

def find_all_seasons() -> List[Season]:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM seasons")
            res = cursor.fetchall()
            all_seasons = [Season(*row) for row in res]  # Unpacking row values into Season
            return all_seasons

def get_season_by_id(season_id: int) -> Optional[Season]:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM seasons WHERE id = %s", (season_id,))
            res = cursor.fetchone()
            return Season(*res) if res else None