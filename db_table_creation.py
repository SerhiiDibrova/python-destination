```python
import os
import psycopg2
from psycopg2 import sql

# Load database connection parameters from environment variables
try:
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
except KeyError as e:
    print(f"Missing environment variable: {e}")
    exit(1)

try:
    # Establish a connection to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
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
        rated INTEGER CHECK (rated > 0)
    )
    """

    # Check if the 'recipes' table exists and create it if not
    cur.execute(sql.SQL("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)"), ('recipes',))
    if not cur.fetchone()[0]:
        cur.execute(recipe_table)

    # Check if the 'recipe_rating' table exists and create it if not
    cur.execute(sql.SQL("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)"), ('recipe_rating',))
    if not cur.fetchone()[0]:
        cur.execute(recipe_rating)

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
```