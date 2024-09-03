import json
from enum import Enum
from typing import Any


class StatusCode(Enum):
    OK = 200
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500


class Response:
    """Basic response data."""

    def __init__(self, status: StatusCode, data: Any):
        self.status_code = status.value
        self.data = data

    def data_pass_with_status(self) -> tuple[str, int]:
        try:
            serializer = json.dumps(self.data)
        except (TypeError, ValueError) as e:
            raise ValueError("Failed to serialize data") from e

        return serializer, self.status_code