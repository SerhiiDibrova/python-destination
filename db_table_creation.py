import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

load_dotenv()

# Establish a connection to the database using environment variables
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME", ""),
    user=os.getenv("DB_USER", ""),
    password=os.getenv("DB_PASSWORD", ""),
    host=os.getenv("DB_HOST", ""),
    port=int(os.getenv("DB_PORT", ""))
)

try:
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

    # Check if the 'recipes' table exists and create it if not
    cur.execute("SELECT to_regclass('recipes') IS NOT NULL")
    if not cur.fetchone()[0]:
        cur.execute(sql.SQL(recipe_table))

    # Check if the 'recipe_rating' table exists and create it if not
    cur.execute("SELECT to_regclass('recipe_rating') IS NOT NULL")
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
    conn.close()