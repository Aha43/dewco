from datetime import datetime
from typing import List

from .domain.util import object_to_str


class Result:
    """Result of a request to a device"""
    def __init__(self, ok: bool, message: str, data: List[object]):
        self.time = object_to_str(datetime.now())
        self.utc = object_to_str(datetime.utcnow())
        self.ok = object_to_str(ok)
        self.message = object_to_str(message)
        if data != None:
            self.data = data.copy()

    @classmethod
    def from_error(cls, message: str):
        return cls(False, message, None)

    @classmethod
    def from_success(cls, data: List[object] = None):
        return cls(True, None, data)
