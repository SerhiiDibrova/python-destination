import datetime
from db.database_connection import db_connection, db

try:
    data = [
        ('Hello', 10, 3, True, datetime.datetime.now()),
        ('Recipe Two', 8, 3, True, datetime.datetime.now())
    ]

    query = "INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)"

    if db_connection is not None and db is not None:
        db.executemany(query, data)
        db_connection.commit()
except Exception as e:
    if db_connection is not None:
        db_connection.rollback()
    print(f"An error occurred: {e}")
if db is not None:
    db.close()
if db_connection is not None:
    db_connection.close()