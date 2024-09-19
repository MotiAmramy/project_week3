from models.Player import Player
from repository.database import get_db_connection
from typing import List, Optional


def create_table_player():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    position VARCHAR(6) NOT NULL
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()


def create_player(player: Player) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        print(cursor)
        cursor.execute("""
            INSERT INTO players (name, position)
            VALUES (%s, %s) RETURNING id
        """, (player.name, player.position))
        player_id = cursor.fetchone()['id']  # Fetch the newly created player's ID
        connection.commit()  # Commit the transaction
        return player_id


def find_all_players():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players")
        players = cursor.fetchall()
        all_players = [Player(**f) for f in players]
        return all_players


def find_player_by_id(player_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM players WHERE id = %s", (player_id,))
    player = cursor.fetchone()
    cursor.close()
    connection.close()
    return player

def get_players_by_name(p_name):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players WHERE name = %s", (p_name,))
        player = cursor.fetchone()['id']
        return player





# def delete_user( id : int) -> int:
#     with get_db_connection() as connection, connection.cursor() as cursor:
#         cursor.execute("DELETE FROM users WHERE id = %s RETURNING id", (id,))
#         _id = cursor.fetchone()['id']
#         return _id
#
#
#
# def update_user(user : User) -> int:
#     with get_db_connection() as connection, connection.cursor() as cursor:
#         cursor.execute("UPDATE users SET first = %s, last = %s, email = %s WHERE id = %s RETURNING id", (user.first, user.last, user.email, user.id))
#         _id = cursor.fetchone()["id"]
#         return _id


