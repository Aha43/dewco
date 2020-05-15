import numbers
from datetime import datetime
from typing import List

def to_str(o: object) -> str:
    if o == None:
        return ""
    return str(o).lower()

class Value:
    """Represents a named value of a System state"""
    def __init__(self, name: str, value: object, unit: str):
        self.name = to_str(name)
        self.value = to_str(value)
        self.unit = to_str(unit)
        self.write = "false"
        self.type = self.__get_api_value_type(value)

    def __get_api_value_type(self, val: object) -> str:
        if (val == None):
            return ""
        if (isinstance(val, bool)):
            return "boolean"
        if (isinstance(val, numbers.Number)):
            return "number"
        return "string"

    # @classmethod
    # def from_dict(cls, d: dict):
    #     name = dict["name"]
    #     value = dict["value"]
    #     unit = dict["unit"]
    #     type = dict["type"]
    #     write = dict["write"]

    #     pass

    @classmethod
    def read_only(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = to_str(False)
        return retVal

    @classmethod
    def read_write(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = to_str(True)
        return retVal

    

class System:
    """Represent state or desired sub state of a device System"""
    def __init__(self, name: str, ok: bool, message: str, state: List[Value]):
        self.name = to_str(name)
        self.ok = to_str(ok)
        self.message = to_str(message)
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
        self.time = to_str(datetime.now())
        self.utc = to_str(datetime.utcnow())
        self.ok = to_str(ok)
        self.message = to_str(message)
        self.data = []
        if data != None:
            self.data = data.copy()

    @classmethod
    def from_error(cls, message: str):
        return cls(False, message, None)

    @classmethod
    def from_success(cls, data: List[object]):
        return cls(True, None, data)
