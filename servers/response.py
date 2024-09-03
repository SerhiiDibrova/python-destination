import json
from typing import Any, Tuple


class Response:
    """
    A basic response data class.

    Attributes:
        status_code (int): The HTTP status code of the response.
        data (Any): The data to be serialized and returned in the response.
    """

    def __init__(self, status: int, data: Any):
        self.status_code = status
        self.data = data

    def data_pass_with_status(self) -> Tuple[str, int]:
        """
        Serialize the response data with JSON and return it along with the status code.

        Returns:
            tuple[str, int]: A tuple containing the serialized data as a string and the HTTP status code.
        """

        serializer = json.dumps(self.data)
        return serializer, self.status_code