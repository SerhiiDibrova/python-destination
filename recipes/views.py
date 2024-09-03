from db.query import fetch_all_recipes
from db.crud import create_recipe_into_db, update_recipe_into_db, delete_recipe_from_db, recipe_rating_into_db
from fastapi.responses import JSONResponse
from fastapi import status


class WelcomeView:

    def get(self):
        data = 'Welcome to HelloFresh'
        return JSONResponse(content={"data": data}, status_code=status.HTTP_200_OK)


class AllRecipes:

    def get(self):
        data = fetch_all_recipes()
        return JSONResponse(content={"data": data}, status_code=status.HTTP_200_OK)


class SingleRecipe:

    def get(self, pk=None):
        recipes = fetch_all_recipes()
        return_data = [recipe for recipe in recipes if recipe['id'] == int(pk)]
        return JSONResponse(content={"data": return_data}, status_code=status.HTTP_200_OK)


class CreateRecipe:

    def post(self, data):
        message, status_code = create_recipe_into_db(data=data)
        return JSONResponse(content={"message": message}, status_code=status_code)


class UpdateRecipe:

    def post(self, data, pk=None):
        data['id'] = pk
        message, status_code = update_recipe_into_db(data)
        return JSONResponse(content={"message": message}, status_code=status_code)


class DeleteRecipe:

    def delete(self, pk=None):
        message, status_code = delete_recipe_from_db({"id": pk})
        return JSONResponse(content={"message": message}, status_code=status_code)


class RecipeRating:

    def post(self, data, pk=None):
        data['id'] = pk
        message, status_code = recipe_rating_into_db(data=data)
        return JSONResponse(content={"message": message}, status_code=status_code)