import psycopg2
from psycopg2 import sql
import logging
import os

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_tables(db_config):
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )

        # Create a cursor object
        cur = conn.cursor()

        recipe_table = """
        CREATE TABLE IF NOT EXISTS recipes (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            pre_time INTEGER CHECK (pre_time > 0),
            difficulty INTEGER CHECK (difficulty > 0),
            vegetarian BOOLEAN,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        recipe_rating = """
        CREATE TABLE IF NOT EXISTS recipe_rating (
            recipe_id INTEGER REFERENCES recipes(id),
            rated INTEGER CHECK(rated > 0)
        )
        """

        # Check if tables exist and create them only if they do not exist
        cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)", ('recipes',))
        if not cur.fetchone()[0]:
            cur.execute(recipe_table)

        cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)", ('recipe_rating',))
        if not cur.fetchone()[0]:
            cur.execute(recipe_rating)

        # Commit the transaction
        conn.commit()

    except psycopg2.Error as e:
        logger.error(f"Failed to create tables: {e}")
        raise

    finally:
        # Close the cursor and connection
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    db_config = {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT')
    }

    create_tables(db_config)