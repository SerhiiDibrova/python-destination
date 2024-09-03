from datetime import datetime
from db.database_connection import db_connection, db

def insert_recipe(name: str, pre_time: int, difficulty: int, vegetarian: bool) -> None:
    try:
        db.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
                   (name, pre_time, difficulty, vegetarian, datetime.now()))
        db_connection.commit()
    except Exception as e:
        db_connection.rollback()
        print(f"An error occurred: {e}")
    finally:
        db_connection.close()
        db.close()

# Example usage
insert_recipe('Hello', 10, 3, True)
insert_recipe('Recipe Two', 8, 3, True)