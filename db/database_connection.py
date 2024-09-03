import logging
from psycopg2 import connect, OperationalError, Error
from psycopg2.extras import DictCursor
from typing import Dict, Tuple

# Configure the logger
logging.basicConfig(level=logging.ERROR)

def create_database_connection(database_config: Dict[str, str]) -> Tuple[object, object]:
    """
    Creates a connection to the PostgreSQL database.

    Args:
        database_config (dict): A dictionary containing the database configuration.
            It should have the following keys: host, database, user, password.

    Returns:
        tuple: A tuple containing the database connection and cursor objects.
    """

    try:
        # Connect to an existing database
        db_connection = connect(**database_config)
        
        # Open a cursor to perform database operations
        db_cursor = db_connection.cursor(cursor_factory=DictCursor)
        
        return db_connection, db_cursor
    
    except (OperationalError, Error) as e:
        logging.error(f"Failed to connect to the database: {e}")
        raise

from config import DATABASE  # Update import statement to reflect changes in library names or modules

db_connection, db_cursor = create_database_connection(DATABASE)