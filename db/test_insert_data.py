import logging
from datetime import datetime
from db.database_connection import db_connection, db

# Set up logging configuration
logging.basicConfig(level=logging.ERROR)

now = datetime.now()

recipes_to_insert = [
    ('Hello', 10, 3, True),
    ('Recipe Two', 8, 3, True)
]

try:
    with db_connection as connection:
        for recipe in recipes_to_insert:
            try:
                db.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
                           (*recipe, now))
            except Exception as e:
                logging.error(f"Error inserting recipe: {e}")
except Exception as e:
    logging.error(f"Error committing changes or closing database connection: {e}")

try:
    db.close()
except Exception as e:
    logging.error(f"Error closing database object: {e}")