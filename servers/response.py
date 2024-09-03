import json
from typing import Any, Tuple


class Response:
    """
    A class representing a basic response data.

    Attributes:
        status_code (int): The HTTP status code of the response.
        data (Any): The data to be serialized and returned with the status code.
    """

    def __init__(self, status: int, data: Any):
        """
        Initializes a Response object with a given status code and data.

        Args:
            status (int): The HTTP status code of the response.
            data (Any): The data to be serialized and returned with the status code.
        """
        self.status_code = status
        self.data = data

    def data_pass_with_status(self) -> Tuple[str, int]:
        """
        Serializes the data using JSON and returns it along with the status code.

        Returns:
            Tuple[str, int]: A tuple containing the serialized data as a string and the status code.
        """
        try:
            serializer = json.dumps(self.data)
        except TypeError as e:
            raise ValueError("Failed to serialize data") from e

        return serializer, self.status_code