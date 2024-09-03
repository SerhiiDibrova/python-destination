from psycopg2 import connect
from psycopg2.extras import DictCursor
import logging

from settings.settings import DATABASE

__author__ = "Vubon Roy"

def create_db_connection():
    try:
        # Connect to an existing database
        db_connection = connect(**DATABASE, cursor_factory=DictCursor)
        
        # Open a cursor to perform database operations
        db = db_connection.cursor()
        return db_connection, db
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def main():
    try:
        db_connection, db = create_db_connection()
        yield db
    finally:
        if 'db' in locals():
            db.close()
        if 'db_connection' in locals():
            db_connection.close()

if __name__ == "__main__":
    with main() as db:
        # Perform database operations using the cursor
        pass