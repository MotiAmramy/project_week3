from models.Season import Season
from repository.database import get_db_connection
from  typing import List, Optional



def create_seasons_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS seasons (
        id SERIAL PRIMARY KEY,
        player_id INT,
        season INT,
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
        team VARCHAR(255),
        FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
    )
""")
    conn.commit()
    cur.close()
    conn.close()



def create_season(seasons : Season) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO seasons (
        player_id, season, position, age, games,
        games_started, minutes_pg, field_goals, field_attempts, field_percent,
        three_fg, three_attempts, three_percent,
         two_fg,  two_attempts, two_percent,
         effective_fg_percent, ft,  ft_attempts,
        ft_percent,  offensive_rb, defensive_rb, total_rb, assists,
        steals, blocks, turnovers,  personal_fouls, points, team
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    ) returning id
    """, (seasons.player_id,seasons.season,seasons.position,seasons.age,seasons.games,
          seasons.games_started,seasons.minutes_pg,seasons.field_goals,seasons.field_attempts,seasons.field_percent,
          seasons.three_fg,seasons.three_attempts,seasons.three_percent,
          seasons.two_fg,seasons.two_attempts,seasons.two_percent,
          seasons.effective_fg_percent, seasons.ft, seasons.ft_attempts,
          seasons.ft_percent, seasons.offensive_rb,
          seasons.defensive_rb, seasons.total_rb, seasons.assists,
          seasons.steals,
          seasons.blocks, seasons.turnovers, seasons.personal_fouls,
          seasons.points,seasons.team
          ))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
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