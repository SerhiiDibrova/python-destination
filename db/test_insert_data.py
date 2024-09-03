from datetime import datetime
from db.database_connection import db_connection, db

try:
    with db_connection.cursor() as cursor:
        cursor.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
                       ('Hello', 10, 3, True, datetime.now()))
        cursor.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
                       ('Recipe Two', 8, 3, True, datetime.now()))

    db_connection.commit()
except Exception as e:
    db_connection.rollback()
    print(f"An error occurred: {e}")
finally:
    db_connection.close()