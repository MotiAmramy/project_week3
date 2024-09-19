from api.api_request import get_api_players
from repository.database import get_db_connection
from repository.player_repository import find_all_players, create_table_player
from repository.season_repository import find_all_seasons, create_season, create_seasons_tables
from service.player_service import convert_to_player, convert_to_season


def create_player_and_season(year):
    data = get_api_players(year)
    print(data)
    for d in data:
        p_id = convert_to_player(d)
        convert_to_season(d,p_id)
def drop_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(""" 
            DROP TABLE IF EXISTS seasons; 
            DROP TABLE IF EXISTS players;
            DROP TABLE IF EXISTS groups; 

        """)
    connection.commit()
    cursor.close()
    connection.close()



if __name__ == '__main__':
    print("Fd")
    drop_table()
    create_table_player()
    create_seasons_tables()
    create_player_and_season(2024)
    print(find_all_players())
    print(find_all_seasons())


