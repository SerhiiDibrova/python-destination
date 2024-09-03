from db.database_connection import db
from typing import List, Dict
import logging
import json


def fetch_all_recipes() -> List[Dict]:
    """
    Fetches all recipes from the database.

    Returns:
        A list of dictionaries containing recipe information.
    """
    try:
        db.execute(
            "SELECT recipes.id, name, pre_time, difficulty, vegetarian, created_at, ROUND(AVG(rated),2) "
            "FROM recipes LEFT JOIN recipe_rating ON recipe_id=id GROUP BY recipes.id ORDER BY id ASC")
        
        recipes = []
        for item in db.fetchall():
            data = {
                'id': item[0],
                'name': item[1],
                'pre_time': item[2],
                'difficulty': item[3],
                'vegetarian': item[4],
                'created_at': item[5].strftime('%Y-%m-%dT%H:%M:%S') if item[5] else None,
                'average_rating': str(item[6])
            }
            recipes.append(data)
        return recipes
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise