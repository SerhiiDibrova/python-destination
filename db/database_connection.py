from psycopg2 import connect, OperationalError
from psycopg2.extras import DictCursor
import logging

from settings.settings import DATABASE

# Set up logging configuration
logging.basicConfig(level=logging.ERROR)

def create_db_connection():
    try:
        # Connect to an existing database
        db_connection = connect(**DATABASE, cursor_factory=DictCursor)
        
        # Open a cursor to perform database operations
        db = db_connection.cursor()
        return db
    except OperationalError as e:
        logging.error(f"Error connecting to the database: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Create a connection to the database
db = create_db_connection()