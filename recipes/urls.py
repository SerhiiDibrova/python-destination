import re
from http import HTTPStatus

# Define constants for HTTP status codes and error messages
HTTP_404_NOT_FOUND = 404
HTTP_401_UNAUTHORIZED = 401
URL_NOT_FOUND = "URL not found"
UNAUTHORIZED = "Unauthorized"

class Recipes:
    def __init__(self):
        self.recipes = {}

    def get(self, pk=None):
        if pk is None:
            return HTTPStatus.OK, list(self.recipes.values())
        elif pk in self.recipes:
            return HTTPStatus.OK, self.recipes[pk]
        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    def post(self, data):
        # Implement recipe creation logic here
        pass

    def delete(self, pk):
        if pk in self.recipes:
            del self.recipes[pk]
            return HTTPStatus.OK, {}
        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    def put(self, pk, data):
        # Implement recipe update logic here
        pass

class RecipeRating:
    def __init__(self):
        self.ratings = {}

    def post(self, data, pk):
        # Implement rating creation logic here
        pass

def handle_request(request_type, path, authentication=None, data=None):
    recipes = Recipes()
    recipe_rating = RecipeRating()

    if request_type == 'GET':
        get_pk = re.findall("\d+", path)
        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/recipes/{}'.format(pk), recipes.get(pk=pk)),
            ]

            if any(path in url for url in [p[0] for p in paths]):
                if path == '/recipes/{}'.format(pk):
                    return paths[0][1].status_code, paths[0][1].data
                else:
                    return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        if any(path in url for url in [p[0] for p in paths]):

            if path == '/':
                return HTTPStatus.OK, {}

            elif path == '/recipes':

                return recipes.get().status_code, recipes.get().data

        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'POST':
        get_pk = re.findall("\d+", path)

        if authentication is None and path == '/recipes':
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + "your_secret_key":
            paths = [
                ('/recipes', recipes.post(data)),
            ]

            if any(path in url for url in [p[0] for p in paths]):
                if path == '/recipes':
                    return paths[0][1].status_code, paths[0][1].data

            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        elif authentication is None:
            if get_pk:
                pk = get_pk[0]
                paths = [
                    ('/recipes/{}/rating'.format(pk), recipe_rating.post(data=data, pk=pk)),
                ]

                if any(path in url for url in [p[0] for p in paths]):
                    return paths[0][1].status_code, paths[0][1].data

                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
        else:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

    elif request_type == 'DELETE':
        get_pk = re.findall("\d+", path)

        if authentication is None:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + "your_secret_key":
            if get_pk:
                pk = get_pk[0]
                paths = [
                    ('/recipes/{}'.format(pk), recipes.delete(pk=pk)),
                ]
                if path == '/recipes/{}'.format(pk):
                    return paths[0][1].status_code, paths[0][1].data
                else:
                    return HTTP_404_NOT_FOUND, URL_NOT_FOUND

            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'PUT':
        get_pk = re.findall("\d+", path)

        if authentication is None and path == '/recipes/{}'.format(get_pk[0]):
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + "your_secret_key":
            if get_pk:
                pk = get_pk[0]
                paths = [
                    ('/recipes/{}'.format(pk), recipes.put(pk=pk, data=data)),
                ]

                if any(path in url for url in [p[0] for p in paths]):
                    return paths[0][1].status_code, paths[0][1].data
                else:
                    return HTTP_404_NOT_FOUND, URL_NOT_FOUND