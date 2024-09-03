from db.database_connection import db


def fetch_all_recipes():
    try:
        db.execute(
            "SELECT recipes.id, name, pre_time, difficulty, vegetarian, created_at, ROUND(AVG(rated),2) "
            "FROM recipes LEFT JOIN recipe_rating ON recipe_id=id GROUP BY recipes.id ORDER BY id ASC")

        recipes = []
        result = db.fetchall()
        if result is not None:
            for item in result:
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