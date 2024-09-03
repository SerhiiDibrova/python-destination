import base64


class DefaultUser:
    """Default user for authentication testing purpose."""

    key = ""

    def set_auth(self, username: str, password: str) -> None:
        """
        Sets the authentication key.

        Args:
            username (str): The username.
            password (str): The password.

        Raises:
            ValueError: If either the username or password is empty.
        """
        if not username or not password:
            raise ValueError("Username and password cannot be empty")
        self.key = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('ascii')

    def get_auth_key(self) -> str:
        """Gets the authentication key.

        Returns:
            str: The authentication key.
        """
        return self.key


def user_data() -> str:
    """Generates user data for testing purposes.

    Returns:
        str: The generated user data.
    """
    user = DefaultUser()
    user.set_auth('vubon', '123456')
    return user.get_auth_key()