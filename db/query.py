from db.database_connection import db
import json
from datetime import datetime


def fetch_all_recipes():
    """
    Fetches all recipes from the database, including their average rating.

    Returns:
        list: A list of dictionaries containing recipe data.
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
                'created_at': datetime.isoformat(item[5]),
                'average_rating': str(item[6])
            }
            recipes.append(data)
        return recipes
    except Exception as e:
        print(f"An error occurred: {e}")
        return []