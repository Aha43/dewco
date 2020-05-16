import numbers
from datetime import datetime
from typing import Dict, List

from .domain_util import get_dict_value, object_to_str, str_to_bool, str_to_float


class Value:
    """Represents a named value of a System state"""
    def __init__(self, name: str, value: object, unit: str):
        self.name = object_to_str(name)
        self.value = object_to_str(value)
        self.unit = object_to_str(unit)
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

    @classmethod
    def from_dict(cls, d: dict):
        name = get_dict_value("name", d)
        value = get_dict_value("value", d)
        unit = get_dict_value("unit", d)
        retVal = cls(name, value, unit)
        retVal.write = get_dict_value("write", d)
        retVal.type = get_dict_value("type", d)
        return retVal

    @classmethod
    def read_only(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = object_to_str(False)
        return retVal

    @classmethod
    def read_write(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = object_to_str(True)
        return retVal

def get_state(dicts: List[Dict]) -> List[Value]:
    retVal = []
    for d in dicts:
        retVal.append(Value.from_dict(d))
    return retVal

class System:
    """Represent state or desired sub state of a device System"""
    def __init__(self, name: str, ok: bool, message: str, state: List[Value], action: str = "read"):
        self.name = object_to_str(name)
        self.ok = object_to_str(ok)
        self.message = object_to_str(message)
        self.state = []
        if state != None:
            self.state = state.copy()
        self.action = action
        
    @classmethod
    def from_success(cls, name: str, state: List[Value]):
        return cls(name, True, None, state)

    @classmethod
    def from_error(cls, name: str, message: str):
        return cls(name, False, message, None)

    @classmethod
    def from_dict(cls, d: dict):
        name = get_dict_value("name", d)
        ok = str_to_bool(get_dict_value("ok", d, "true"))
        message = get_dict_value("message", d)
        stateDicts = []
        if "state" in d:
            stateDicts = d["state"]
        state = get_state(stateDicts)
        action = get_dict_value("action", d, "read")
        retVal = cls(name, ok, message, state, action)
        return retVal

    def get_state_variable(self, name: str) -> Value:
        for v in self.state:
            if v.name == name:
                return v
        return None

    def get_state_value(self, name: str) -> str:
        var = self.get_state_variable(name)
        if var:
            return var.value
        return ""
