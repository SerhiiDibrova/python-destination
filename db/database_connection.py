from psycopg2 import connect
from psycopg2.extras import DictCursor
import sys
import logging

__author__ = "Vubon Roy"

try:
    from settings.settings import DATABASE
except ImportError as e:
    logging.error(f"Error importing DATABASE settings: {e}")
    sys.exit(1)

# Connect to an existing database
db_connection = connect(**DATABASE, cursor_factory=DictCursor)

# Open a cursor to perform database operations
db = db_connection.cursor()