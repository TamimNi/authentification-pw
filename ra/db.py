# db.py
import psycopg2
from config import Config

def get_db_connection():
    conn = psycopg2.connect(
        dbname=Config.DATABASE_NAME,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD,
        host=Config.DATABASE_HOST,
        port=Config.DATABASE_PORT
    )
    return conn
