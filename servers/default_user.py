import base64
from typing import Optional


class DefaultUser:
    """Default user for authentication testing purposes."""

    key: str = ""

    def set_auth(self, username: str, password: str) -> None:
        """
        Sets the authorization key using the provided username and password.

        Args:
            username (str): The username to use.
            password (str): The password to use.
        """
        self.key = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode(
            "ascii"
        )

    def get_auth_key(self) -> Optional[str]:
        """
        Retrieves the authorization key.

        Returns:
            str: The authorization key, or None if not set.
        """
        return self.key


def generate_user_data() -> str:
    """Generates user data for authentication testing purposes."""
    user = DefaultUser()
    user.set_auth("vubon", "123456")
    auth_key = user.get_auth_key()
    if auth_key is None:
        raise ValueError("Authorization key not set")
    return auth_key