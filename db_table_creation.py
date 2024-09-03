import os
import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor

# Load database connection parameters from environment variables
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')

if not all([DB_NAME, DB_USER, DB_PASSWORD, DB_HOST]):
    raise ValueError("All database connection environment variables must be set")

try:
    # Establish a connection to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )

    # Create a cursor object with DictCursor to return rows as dictionaries
    cur = conn.cursor(cursor_factory=DictCursor)

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

    # Check if the 'recipes' table exists and create it if not
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='recipes')")
    if not cur.fetchone()[0]:
        cur.execute(sql.SQL(recipe_table))

    # Check if the 'recipe_rating' table exists and create it if not
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='recipe_rating')")
    if not cur.fetchone()[0]:
        cur.execute(sql.SQL(recipe_rating))

    # Commit the changes
    conn.commit()

except psycopg2.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()