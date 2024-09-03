"""
All response messages
created_date: 2023-03-15
last_update: 2023-03-15
"""
__author__ = 'Vubon Roy'
__version__ = '1.0.0'

# No imports are required for this file.

# common messages
URL_NOT_FOUND: dict[str, str] = {"message": "URL not found"}
DATA_NOT_FOUND: dict[str, str] = {"message": "Data not found"}
INVALID_REQUEST: dict[str, str] = {"message": "Invalid request"}

# user related messages
UNAUTHORIZED: dict[str, str] = {"message": "Unauthorized"}

# Recipe related messages
RECIPE_CREATED: dict[str, str] = {"message": "Recipe created"}
RECIPE_UPDATED: dict[str, str] = {"message": "Recipe Updated"}
RECIPE_DELETED: dict[str, str] = {"message": "Recipe Deleted"}
RECIPE_RATING: dict[str, str] = {"message": "Rating added"}