import base64
from typing import Optional


class DefaultUser:
    """Default user for authentication testing purpose."""

    key: str = ""

    def set_auth(self, username: str, password: str) -> None:
        """
        Sets the authentication key.

        Args:
            username (str): The username.
            password (str): The password.

        Raises:
            ValueError: If an error occurs during base64 encoding.
        """
        try:
            self.key = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('ascii')
        except Exception as e:
            raise ValueError(f"An error occurred: {e}")

    def get_auth_key(self) -> str:
        """
        Gets the authentication key.

        Returns:
            str: The authentication key.
        """
        return self.key


def generate_default_user_data() -> str:
    """Generates default user data."""
    user = DefaultUser()
    user.set_auth('vubon', '123456')
    return user.get_auth_key()