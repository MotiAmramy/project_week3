import pytest
from models.Group import Group
from repository.database import get_db_connection
from repository.group_repository import create_table_group, create_group, find_all_groups, get_group_by_id


@pytest.fixture(scope="module")
def setup_group_database():
    # Create the groups table
    create_table_group()  # Assume you have this function
    yield
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(""" 
        DROP TABLE IF EXISTS groups; 
    """)
    connection.commit()
    cursor.close()
    connection.close()

def test_create_group(setup_group_database):
    new_group = Group(id=None, name="Group A", player1=4, player2=4, player3=1, player4=1, player5=0)
    create = create_group(new_group)
    assert create

def test_find_all_groups(setup_group_database):
    all_groups = find_all_groups()
    assert len(all_groups) > 0

def test_find_group_by_id(setup_group_database):
    group = get_group_by_id(1)  # Adjust based on the expected ID
    assert group is not None