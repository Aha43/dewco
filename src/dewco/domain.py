import numbers
from datetime import datetime
from typing import List


class Value:
    """Represents a named value of a System state"""
    def __init__(self, name: str, value: object, unit: str):
        self.name = name
        self.value = str(value)
        self.unit = unit
        self.write = False
        self.type = self.__get_api_value_type(value)

    def __get_api_value_type(self, val: object) -> str:
        if (val == None):
            return "null"
        if (isinstance(val, bool)):
            return "boolean"
        if (isinstance(val, numbers.Number)):
            return "number"
        return "string"

    @classmethod
    def read_only(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = False
        return retVal

    @classmethod
    def read_write(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = True
        return retVal

class System:
    """Represent state or desired sub state of a device System"""
    def __init__(self, name: str, ok: bool, message: str, state: List[Value]):
        self.name = name
        self.ok = ok
        self.message = message
        self.state = []
        if state != None:
            self.state = state.copy()

    @classmethod
    def from_success(cls, name: str, state: List[Value]):
        return cls(name, True, None, state)

    @classmethod
    def from_error(cls, name: str, message: str):
        return cls(name, False, message, None)

class Result:
    """Result of a request to a device"""
    def __init__(self, ok: bool, message: str, data: List[object]):
        self.time = str(datetime.now())
        self.utc = str(datetime.utcnow())
        self.ok = ok
        self.message = message
        self.data = []
        if data != None:
            self.data = data.copy()

    @classmethod
    def from_error(cls, message: str):
        return cls(False, message, None)

    @classmethod
    def from_success(cls, data: List[object]):
        return cls(True, None, data)
