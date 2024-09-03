import datetime
from db.database_connection import db_connection, db

try:
    db.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
               ('Hello', 10, 3, True, datetime.datetime.now()))
    db.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
               ('Recipe Two', 8, 3, True, datetime.datetime.now()))

    db_connection.commit()
except Exception as e:
    db_connection.rollback()
    print(f"An error occurred: {e}")
finally:
    db_connection.close()
    db.close()