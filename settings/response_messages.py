"""
Response Messages Module
------------------------

This module contains all response messages used throughout the application.

Author: Vubon Roy
Version: 1.0.0
"""

__author__ = 'Vubon Roy'
__version__ = '1.0.0'

# common messages
URL_NOT_FOUND: dict[str, str] = {"message": "URL not found", "description": "The requested URL was not found on the server."}
DATA_NOT_FOUND: dict[str, str] = {"message": "Data not found", "description": "The requested data was not found in the database."}
INVALID_REQUEST: dict[str, str] = {"message": "Invalid request", "description": "The request was invalid or cannot be processed."}

# user related messages
UNAUTHORIZED: dict[str, str] = {"message": "Unauthorized", "description": "You are not authorized to access this resource."}

# Recipe related messages
RECIPE_CREATED: dict[str, str] = {"message": "Recipe created", "description": "A new recipe has been successfully created."}
RECIPE_UPDATED: dict[str, str] = {"message": "Recipe Updated", "description": "The recipe has been successfully updated."}
RECIPE_DELETED: dict[str, str] = {"message": "Recipe Deleted", "description": "The recipe has been successfully deleted."}
RECIPE_RATING: dict[str, str] = {"message": "Rating added", "description": "A new rating has been successfully added to the recipe."}