"""
All response messages
created_date: 08-08-2018
last_update: 08-08-2018
"""

__author__ = 'Vubon Roy'
__version__ = '0.0.1'

# No imports are required for this file.

class ResponseMessages:
    """Container class for response messages."""

    def __init__(self) -> None:
        self.common_messages: dict[str, str] = {}
        self.user_related_messages: dict[str, str] = {}
        self.recipe_related_messages: dict[str, str] = {}

    def validate_message(self, message: dict[str, str]) -> None:
        """Validate the message dictionary."""
        if not isinstance(message, dict):
            raise ValueError("Message must be a dictionary")
        if "message" not in message:
            raise ValueError("Message dictionary must contain 'message' key")

    @property
    def url_not_found(self) -> dict[str, str]:
        """URL not found message."""
        self.common_messages["url_not_found"] = {"message": "URL not found"}
        return self.common_messages["url_not_found"]

    @property
    def data_not_found(self) -> dict[str, str]:
        """Data not found message."""
        self.common_messages["data_not_found"] = {"message": "Data not found"}
        return self.common_messages["data_not_found"]

    @property
    def invalid_request(self) -> dict[str, str]:
        """Invalid request message."""
        self.common_messages["invalid_request"] = {"message": "Invalid request"}
        return self.common_messages["invalid_request"]

    @property
    def unauthorized(self) -> dict[str, str]:
        """Unauthorized message."""
        self.user_related_messages["unauthorized"] = {"message": "Unauthorized"}
        return self.user_related_messages["unauthorized"]

    @property
    def recipe_created(self) -> dict[str, str]:
        """Recipe created message."""
        self.recipe_related_messages["recipe_created"] = {"message": "Recipe created"}
        return self.recipe_related_messages["recipe_created"]

    @property
    def recipe_updated(self) -> dict[str, str]:
        """Recipe updated message."""
        self.recipe_related_messages["recipe_updated"] = {"message": "Recipe Updated"}
        return self.recipe_related_messages["recipe_updated"]

    @property
    def recipe_deleted(self) -> dict[str, str]:
        """Recipe deleted message."""
        self.recipe_related_messages["recipe_deleted"] = {"message": "Recipe Deleted"}
        return self.recipe_related_messages["recipe_deleted"]

    @property
    def recipe_rating(self) -> dict[str, str]:
        """Recipe rating message."""
        self.recipe_related_messages["recipe_rating"] = {"message": "Rating added"}
        return self.recipe_related_messages["recipe_rating"]

response_messages = ResponseMessages()

# Validate messages
response_messages.validate_message(response_messages.url_not_found)
response_messages.validate_message(response_messages.data_not_found)
response_messages.validate_message(response_messages.invalid_request)
response_messages.validate_message(response_messages.unauthorized)
response_messages.validate_message(response_messages.recipe_created)
response_messages.validate_message(response_messages.recipe_updated)
response_messages.validate_message(response_messages.recipe_deleted)
response_messages.validate_message(response_messages.recipe_rating)