import re
from http import HTTPStatus
from typing import Tuple, Callable

class Response:
    def __init__(self, status: int = 200, data: dict = None):
        self.status = status
        self.data = data


def welcome() -> str:
    return "Welcome"


def recipes_get() -> list:
    # Replace with actual implementation
    return []


def recipe_get(pk: int) -> dict:
    # Replace with actual implementation
    return {}


def create_recipe_post(data: dict) -> dict:
    # Replace with actual implementation
    return data


def recipe_rating_post(data: dict, pk: int) -> dict:
    # Replace with actual implementation
    return data


def update_recipe_put(pk: int) -> dict:
    # Replace with actual implementation
    return {}


def delete_recipe_delete(pk: int) -> None:
    # Replace with actual implementation
    pass


def router(request_type: str, path: str, authentication: str = None, data: dict = None) -> Response:
    get_pk = re.findall("\d+", path)

    paths_get = [
        (r'^/$', welcome),
        (r'^/recipes$', recipes_get),
    ]
    if get_pk:
        pk = get_pk[0]
        paths_get = [
            (rf'^/recipes/{pk}$', recipe_get(pk=pk)),
        ]

    for url, view in paths_get:
        if re.match(url, path):
            return Response(view())

    return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})

    elif request_type == 'POST':
        get_pk = re.findall("\d+", path)

        key = "your_secret_key_here"

        if authentication is None and path == '/recipes':
            return Response(status=HTTPStatus.UNAUTHORIZED, data={'error': 'UNAUTHORIZED'})

        elif authentication == f'Basic {key}':
            paths_post = [
                (r'^/recipes$', create_recipe_post(data=data)),
            ]

            for url, view in paths_post:
                if re.match(url, path):
                    return Response(view())

            return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})

        elif authentication is None:
            if get_pk:
                pk = get_pk[0]
                paths_post = [
                    (rf'^/recipes/{pk}/rating$', recipe_rating_post(data=data, pk=pk)),
                ]

                for url, view in paths_post:
                    if re.match(url, path):
                        return Response(view())

                return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})

            return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})
        else:
            return Response(status=HTTPStatus.UNAUTHORIZED, data={'error': 'UNAUTHORIZED'})

    elif request_type == 'PUT':
        get_pk = re.findall("\d+", path)

        key = "your_secret_key_here"

        if authentication is None:
            return Response(status=HTTPStatus.UNAUTHORIZED, data={'error': 'UNAUTHORIZED'})

        elif authentication == f'Basic {key}':
            if get_pk:
                pk = get_pk[0]
                paths_put = [
                    (rf'^/recipes/{pk}$', update_recipe_put(pk=pk)),
                ]
                for url, view in paths_put:
                    if re.match(url, path):
                        return Response(view())

                return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})

            return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})
        else:
            return Response(status=HTTPStatus.UNAUTHORIZED, data={'error': 'UNAUTHORIZED'})

    elif request_type == 'DELETE':
        get_pk = re.findall("\d+", path)

        key = "your_secret_key_here"

        if authentication is None:
            return Response(status=HTTPStatus.UNAUTHORIZED, data={'error': 'UNAUTHORIZED'})

        elif authentication == f'Basic {key}':
            if get_pk:
                pk = get_pk[0]
                paths_delete = [
                    (rf'^/recipes/{pk}$', delete_recipe_delete(pk=pk)),
                ]
                for url, view in paths_delete:
                    if re.match(url, path):
                        return Response(view())

                return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})

            return Response(status=HTTPStatus.NOT_FOUND, data={'error': 'URL_NOT_FOUND'})
        else:
            return Response(status=HTTPStatus.UNAUTHORIZED, data={'error': 'UNAUTHORIZED'})