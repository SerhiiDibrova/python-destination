from db.database_connection import db
from typing import List, Dict


def fetch_all_recipes(db_connection: object) -> List[Dict]:
    """
    Fetches all recipes from the database.

    Args:
        db_connection (object): The database connection object.

    Returns:
        A list of dictionaries containing recipe information.
    """
    try:
        db_connection.execute(
            "SELECT recipes.id, name, pre_time, difficulty, vegetarian, created_at, ROUND(AVG(rated),2) "
            "FROM recipes LEFT JOIN recipe_rating ON recipe_id=id GROUP BY recipes.id ORDER BY id ASC")

        if db_connection.rowcount == -1:
            raise Exception("Failed to execute query")

        recipes = []
        for item in db_connection.fetchall():
            data = {
                'id': item[0],
                'name': item[1],
                'pre_time': item[2],
                'difficulty': item[3],
                'vegetarian': item[4],
                'created_at': item[5].strftime('%Y-%m-%dT%H:%M:%S'),
                'average_rating': str(item[6])
            }
            recipes.append(data)
        return recipes
    except Exception as e:
        print(f"An error occurred: {e}")
        return []