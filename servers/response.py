import json
from typing import Dict, Any


class Response:
    """
    A basic response data class.

    Attributes:
        status_code (int): The HTTP status code of the response.
        data (Dict[str, Any]): The data to be serialized and returned in the response.
    """

    def __init__(self, status: int, data: Dict[str, Any]):
        if not isinstance(status, int) or not 100 <= status < 600:
            raise ValueError("Invalid HTTP status code")
        self.status_code = status
        self.data = data

    def data_pass_with_status(self) -> tuple[str, int]:
        """
        Serialize the response data with JSON and return it along with the status code.

        Returns:
            tuple[str, int]: A tuple containing the serialized data as a string and the HTTP status code.
        """

        try:
            serializer = json.dumps(self.data)
        except TypeError as e:
            # Handle potential exceptions during JSON serialization
            raise ValueError(f"Error serializing data: {e}") from e

        return serializer, self.status_code