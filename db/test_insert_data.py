```python
from datetime import datetime
import psycopg2
from psycopg2 import Error
from db.database_connection import create_db_connection, get_db_cursor

def insert_recipe(name, pre_time, difficulty, vegetarian):
    try:
        # Create a database connection and cursor object
        db_connection = create_db_connection()
        cursor = get_db_cursor(db_connection)

        # SQL query to insert data into recipes table
        insert_query = "INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)"

        # Using parameterized queries to prevent SQL injection attacks
        now = datetime.now()
        cursor.execute(insert_query, (name, pre_time, difficulty, vegetarian, now))

        # Commit the transaction
        db_connection.commit()

    except Error as e:
        # Rollback the transaction if an error occurs
        db_connection.rollback()
        print(f"An error occurred: {e}")

    finally:
        # Ensure the database connection is properly closed
        if db_connection:
            cursor.close()
            db_connection.close()


# Example usage of the insert_recipe function
if __name__ == "__main__":
    try:
        insert_recipe('Hello', 10, 3, True)
        insert_recipe('Recipe Two', 8, 3, True)

    except Exception as e:
        print(f"An error occurred: {e}")
```