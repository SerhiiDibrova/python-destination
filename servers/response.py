import json
from typing import Any


class Response:
    """
    A class representing a basic response data.

    Attributes:
        status_code (int): The HTTP status code of the response.
        data (Any): The data to be serialized and returned in the response.
    """

    def __init__(self, status: int, data: Any):
        if not isinstance(status, int):
            raise TypeError("Status must be an integer.")
        self.status_code = status
        self.data = data

    def data_pass_with_status(self) -> tuple[str, int]:
        """
        Returns a tuple containing the JSON-serialized data and the HTTP status code.

        Returns:
            tuple[str, int]: A tuple with the serialized data as a string and the status code as an integer.
        """
        try:
            serializer = json.dumps(self.data)
        except TypeError as e:
            raise ValueError("Data cannot be serialized.") from e

        return serializer, self.status_code