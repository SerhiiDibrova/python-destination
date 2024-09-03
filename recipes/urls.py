from typing import Tuple, Dict
import re


class WelcomeView:
    def __init__(self):
        self.status_code = 200
        self.data = "Welcome"


class RecipesView:
    def __init__(self):
        self.status_code = 200
        self.data = "Recipes"


class RecipeView:
    def __init__(self, pk: int):
        self.status_code = 200
        self.data = f"Recipe {pk}"


class CreateRecipeView:
    def __init__(self, data: Dict[str, str]):
        self.status_code = 201
        self.data = data


class UpdateRecipeView:
    def __init__(self, pk: int):
        self.status_code = 200
        self.data = f"Updated recipe {pk}"


class DeleteRecipeView:
    def __init__(self, pk: int):
        self.status_code = 204
        self.data = ""


class RecipeRatingView:
    def __init__(self, data: Dict[str, int], pk: int):
        self.status_code = 200
        self.data = {"rating": data["rating"]}


def get_view(request_type: str, path: str, authentication: str, key: str, data: Dict) -> Tuple[int, str]:
    if request_type == 'GET':
        if path == '/':
            return WelcomeView().status_code, WelcomeView().data
        elif path == '/recipes':
            return RecipesView().status_code, RecipesView().data
        elif re.match(r'^/recipes/\d+$', path):
            pk = int(re.findall(r'\d+', path)[0])
            return RecipeView(pk).status_code, RecipeView(pk).data


def post_view(request_type: str, path: str, authentication: str, key: str, data: Dict) -> Tuple[int, str]:
    if request_type == 'POST':
        if path == '/recipes':
            return CreateRecipeView(data).status_code, CreateRecipeView(data).data
        elif re.match(r'^/recipes/\d+/rating$', path):
            pk = int(re.findall(r'\d+', path)[0])
            return RecipeRatingView(data, pk).status_code, RecipeRatingView(data, pk).data


def put_view(request_type: str, path: str, authentication: str, key: str) -> Tuple[int, str]:
    if request_type == 'PUT':
        if re.match(r'^/recipes/\d+$', path):
            pk = int(re.findall(r'\d+', path)[0])
            return UpdateRecipeView(pk).status_code, UpdateRecipeView(pk).data


def delete_view(request_type: str, path: str, authentication: str, key: str) -> Tuple[int, str]:
    if request_type == 'DELETE':
        if re.match(r'^/recipes/\d+$', path):
            pk = int(re.findall(r'\d+', path)[0])
            return DeleteRecipeView(pk).status_code, DeleteRecipeView(pk).data


def router(request_type: str, path: str, authentication: str, key: str, data: Dict = None) -> Tuple[int, str]:
    if request_type == 'GET':
        return get_view(request_type, path, authentication, key, data)

    elif request_type == 'POST':
        return post_view(request_type, path, authentication, key, data)

    elif request_type == 'PUT':
        return put_view(request_type, path, authentication, key)

    elif request_type == 'DELETE':
        return delete_view(request_type, path, authentication, key)