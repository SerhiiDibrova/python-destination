import base64
from typing import Tuple
import os


class DefaultUser:
    """Default user for authentication testing purposes."""

    def __init__(self):
        self.key = ''

    def set_auth(self, username: str, password: str) -> None:
        """
        Sets the authentication key using the provided username and password.

        Args:
            username (str): The username to use for authentication.
            password (str): The password to use for authentication.
        """
        try:
            self.key = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('ascii')
        except Exception as e:
            raise ValueError(f"An error occurred: {e}")

    def get_auth_key(self) -> str:
        """Returns the authentication key."""
        return self.key


def user_data() -> str:
    """
    Generates user data for testing purposes.

    Returns:
        A string containing the authentication key.
    """
    user = DefaultUser()
    # Use environment variables to store and handle passwords securely
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    if not username or not password:
        raise ValueError("Username and password must be set as environment variables")
    user.set_auth(username, password)
    return user.get_auth_key()