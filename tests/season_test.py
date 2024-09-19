import pytest
from models.Season import Season
from repository.database import get_db_connection
from repository.player_repository import create_player, create_table_player
from repository.season_repository import create_table_season, create_season, get_season_by_id, find_all_seasons



@pytest.fixture(scope="module")
def setup_season_database():
    # Create the seasons table
    create_table_player()
    create_table_season()
    yield
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(""" 
            DROP TABLE IF EXISTS seasons; 
        """)
        connection.commit()
    connection.close()

def ccreate_season():
    # Create a new season instance with required fields
    new_season = Season(
        player_id=1,
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

    try:
        # Call the create_season function to insert the new season into the database
        new_id = create_season(new_season)
        print(f"Season created with ID: {new_id}")
        return new_id
    except Exception as e:
        print(f"Error creating season: {e}")
        return None

def test_find_all_seasons(setup_season_database):
    all_seasons = find_all_seasons()
    assert len(all_seasons) > 0

def test_find_season_by_id(setup_season_database):
    season = get_season_by_id(1)
    assert season is not None


