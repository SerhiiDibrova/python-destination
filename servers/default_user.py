import base64
from typing import Tuple


class DefaultUser:
    """Default user for authentication testing purposes."""

    key = ''

    def set_auth(self, username: str, password: str) -> None:
        """
        Sets the authentication key using the provided username and password.

        Args:
            username (str): The username to use.
            password (str): The password to use.

        Raises:
            ValueError: If either username or password is empty.
            TypeError: If either username or password is not a string.
        """
        if not isinstance(username, str) or not isinstance(password, str):
            raise TypeError("Both username and password must be strings.")
        if not username or not password:
            raise ValueError("Neither username nor password can be empty.")

        self.key = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('ascii')

    def get_auth_key(self) -> str:
        """Returns the authentication key."""
        return self.key


def user_data() -> str:
    """
    If you want to change you can change and use same username password
    when you want to create recipe item, delete recipe, update recipe.
    :return: a key
    :rtype: str
    """
    user = DefaultUser()
    # username and password
    try:
        user.set_auth('vubon', '123456')
        return user.get_auth_key()
    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")
        raise