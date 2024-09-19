import pytest
from api.api_request import get_api_players
from models.Player import Player
from repository.database import get_db_connection
from repository.player_repository import create_table_player
from repository.player_repository import create_player, find_all_players, find_player_by_id
from repository.season_repository import create_season, create_table_season
from tests.season_test import ccreate_season


@pytest.fixture(scope="module")
def setup_player_database():
    create_table_player()
    create_table_season()
    yield
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(""" 
        DROP TABLE IF EXISTS players;
        DROP TABLE IF EXISTS groups; 
        DROP TABLE IF EXISTS seasons; 
        
    """)
    connection.commit()
    cursor.close()
    connection.close()

def test_create_player(setup_player_database):
    new_player = Player(id=1, name="enosh", position="f")
    print(new_player)
    create = create_player(new_player)

    assert create

def test_find_all_players(setup_player_database):
    all_players = find_all_players()
    assert len(all_players) > 0

def test_find_player_by_id(setup_player_database):
    player = find_player_by_id(1)
    assert player is not None