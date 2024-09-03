import datetime
from db.database_connection import db_connection, db
from db.query import fetch_all_recipes
from settings.response_messages import RECIPE_CREATED, RECIPE_UPDATED, RECIPE_DELETED, DATA_NOT_FOUND, RECIPE_RATING
import logging


def create_recipe_into_db(data):
    try:
        with db_connection.cursor() as cursor:
            cursor.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
                           (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'], datetime.datetime.now()))
        db_connection.commit()
        status_code = 201
        return RECIPE_CREATED, status_code
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        status_code = 500
        return "Internal Server Error", status_code


def update_recipe_into_db(data):
    try:
        with db_connection.cursor() as cursor:
            cursor.execute("UPDATE recipes SET name=%s, pre_time=%s, difficulty=%s, vegetarian=%s, created_at=%s WHERE id=%s",
                           (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'], datetime.datetime.now(),
                            data['id']))
        db_connection.commit()
        status_code = 200
        return RECIPE_UPDATED, status_code
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        status_code = 500
        return "Internal Server Error", status_code


def delete_recipe_from_db(data):
    try:
        recipes = fetch_all_recipes()
        for recipe in recipes:
            if recipe['id'] == int(data['id']):
                with db_connection.cursor() as cursor:
                    cursor.execute("DELETE FROM recipes WHERE id=%s", (data['id'],))
                db_connection.commit()
                status_code = 200
                return RECIPE_DELETED, status_code
        status_code = 400
        return DATA_NOT_FOUND, status_code
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        status_code = 500
        return "Internal Server Error", status_code


def recipe_rating_into_db(data):
    try:
        recipes = fetch_all_recipes()
        for recipe in recipes:
            if recipe['id'] == int(data['id']):
                with db_connection.cursor() as cursor:
                    cursor.execute("INSERT INTO recipe_rating (recipe_id, rated) VALUES (%s, %s)", (data['id'], data['rated']))
                db_connection.commit()
                status_code = 201
                return RECIPE_RATING, status_code
        status_code = 400
        return DATA_NOT_FOUND, status_code
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        status_code = 500
        return "Internal Server Error", status_code


def close_db_connection():
    db_connection.close()