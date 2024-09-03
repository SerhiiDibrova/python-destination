import base64
from typing import Optional


class DefaultUser:
    """Default user for authentication testing purpose."""

    key: str = ''

    def set_auth(self, username: str, password: str) -> None:
        """
        Sets the authorization key using the provided username and password.

        Args:
            username (str): The username to use.
            password (str): The password to use.
        """
        if not username or not password:
            raise ValueError("Username and password must be provided")
        self.key = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('ascii')

    def get_auth_key(self) -> Optional[str]:
        """
        Retrieves the authorization key.

        Returns:
            str: The authorization key, or None if not set.
        """
        return self.key


def user_data() -> str:
    """Generates user data for authentication testing."""
    user = DefaultUser()
    # username and password
    user.set_auth('vubon', '123456')
    auth_key = user.get_auth_key()
    if auth_key is None:
        raise ValueError("Authorization key not set")
    return auth_key