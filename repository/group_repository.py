from tkinter import Listbox
from typing import List, Optional
from models.Group import Group
from repository.database import get_db_connection


def create_table_group():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    player1 INT,
    player2 INT,
    player3 INT,
    player4 INT,
    player5 INT
)''')

    connection.commit()
    cursor.close()
    connection.close()




def create_group(group: Group) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO groups (name, player1,player2, player3,player4,player5 )
            VALUES (%s, %s) RETURNING id
        """, (group.name, group.player1 ,group.player2 ,group.player3 ,group.player4, group.player5))
        new_id = cursor.fetchone()['id']
        connection.commit()
        return new_id

def find_all_groups() -> List[Group]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM groups")
        res = cursor.fetchall()
        all_groups = [Group(**f) for f in res]
        return all_groups

def get_group_by_id(group_id: int) -> Optional[Group]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM groups WHERE id = %s", (group_id,))
        res = cursor.fetchone()
        return Group(**res) if res else None