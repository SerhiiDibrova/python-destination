```python
import psycopg2
from psycopg2 import sql, errors

def create_tables(conn):
    try:
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

        cur.execute(recipe_table)
        cur.execute(recipe_rating)

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur:
            cur.close()

def main():
    try:
        conn = psycopg2.connect(
            host="your_host",
            database="your_database",
            user="your_username",
            password="your_password"
        )
        
        create_tables(conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
```