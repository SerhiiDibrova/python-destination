from psycopg2 import connect
from psycopg2.extras import DictCursor
import logging

__author__ = "Vubon Roy"

"""
This module establishes a connection to an existing database.

Created at: 28-07-2018
"""

try:
    from settings.settings import DATABASE
except ImportError as e:
    logging.error(f"Failed to import settings: {e}")
    raise

def get_db_connection():
    try:
        # Connect to an existing database with a context manager
        with connect(**DATABASE, cursor_factory=DictCursor) as db_connection:
            return db_connection
    except Exception as e:
        logging.error(f"Failed to establish database connection: {e}")
        raise

def get_db_cursor(db_connection):
    try:
        # Open a cursor to perform database operations
        return db_connection.cursor()
    except Exception as e:
        logging.error(f"Failed to create database cursor: {e}")
        raise

# Establish the database connection and create a cursor
db_connection = get_db_connection()
db = get_db_cursor(db_connection)