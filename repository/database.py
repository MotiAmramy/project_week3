from psycopg2.extras import RealDictCursor
import psycopg2
from config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    try:
        return psycopg2.connect(SQLALCHEMY_DATABASE_URI, cursor_factory=RealDictCursor)
    except Exception as e:
        print(e)
