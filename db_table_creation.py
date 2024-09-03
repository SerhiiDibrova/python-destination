```python
import os
import psycopg2
from psycopg2 import sql, Error
from db.database_connection import create_db_connection, get_db_cursor

def create_tables():
    try:
        # Create a database connection and cursor object
        db_connection = create_db_connection()
        db_cursor = get_db_cursor(db_connection)

        recipe_table = """
            CREATE TABLE IF NOT EXISTS recipes (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                pre_time INTEGER CHECK (pre_time > 0),
                difficulty INTEGER CHECK (difficulty > 0),
                vegetarian BOOLEAN,
                created_at TIMESTAMP
            )
        """

        recipe_rating = """
            CREATE TABLE IF NOT EXISTS recipe_rating (
                recipe_id INTEGER REFERENCES recipes(id),
                rated INTEGER CHECK(rated > 0)
            )
        """

        # Check if the 'recipes' table exists and create it if not
        db_cursor.execute(sql.SQL("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)"), ('recipes',))
        if not db_cursor.fetchone()[0]:
            db_cursor.execute(recipe_table)

        # Check if the 'recipe_rating' table exists and create it if not
        db_cursor.execute(sql.SQL("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)"), ('recipe_rating',))
        if not db_cursor.fetchone()[0]:
            db_cursor.execute(recipe_rating)

        # Commit changes to the database
        db_connection.commit()
    except Error as e:
        print(f"An error occurred: {e}")
    finally:
        if db_connection:
            db_cursor.close()
            db_connection.close()

create_tables()
```