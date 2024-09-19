import pytest
from models.Season import Season
from repository.database import get_db_connection
from repository.season_repository import create_table_season, create_season, get_season_by_id, find_all_seasons



@pytest.fixture(scope="module")
def setup_season_database():
    # Create the seasons table
    create_table_season()
    yield
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(""" 
            DROP TABLE IF EXISTS seasons; 
        """)
        connection.commit()
    connection.close()

def test_create_season(setup_season_database):
    # Create a new season instance with required fields
    new_season = Season(
        player_id=1,  # Assuming there's a player with ID 1
        position="SG",
        age=25,
        games=10,
        games_started=8,
        minutes_pg=30.5,
        field_goals=20,
        field_attempts=50,
        field_percent=0.4,
        three_fg=5,
        three_attempts=15,
        three_percent=0.33,
        two_fg=15,
        two_attempts=35,
        two_percent=0.43,
        effective_fg_percent=0.45,
        ft=10,
        ft_attempts=12,
        ft_percent=0.83,
        offensive_rb=3,
        defensive_rb=7,
        total_rb=10,
        assists=5,
        steals=2,
        blocks=1,
        turnovers=3,
        personal_fouls=4,
        points=50,
        team="CHI",
        season=2024
    )
    create = create_season(new_season, 1)  # Ensure you have a function to create a season
    assert create

def test_find_all_seasons(setup_season_database):
    all_seasons = find_all_seasons()
    assert len(all_seasons) > 0

def test_find_season_by_id(setup_season_database):
    season = get_season_by_id(1)
    assert season is not None