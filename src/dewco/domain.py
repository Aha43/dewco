import json
from .util import get_api_value_type

from datetime import datetime
from typing import List

class Value:
    """Represents a named value of a System state"""
    def __init__(self, name: str, value: object, unit: str):
        self.name = name
        self.value = str(value)
        self.unit = unit
        self.write = False
        self.type = get_api_value_type(value)

    @classmethod
    def readOnly(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = False
        return retVal

    @classmethod
    def readWrite(cls, name: str, value: object, unit: str = None):
        retVal = cls(name, value, unit)
        retVal.write = True
        return retVal

class System:
    """Represent state or desired sub state of a device System"""
    def __init__(self, id: int, parent: id, name: str, ok: bool, message: str, state: List[Value]):
        self.id = id
        self.parent = parent
        self.name = name
        self.ok = ok
        self.message = message
        self.state = []
        if state != None:
            self.state = state.copy()

    @classmethod
    def fromSuccess(cls, name: str, state: List[Value], id: int = 0, parent = -1):
        return cls(id, parent, name, True, None, state)

    @classmethod
    def fromError(cls, name: str, message: str, id: int = 0, parent = -1):
        return cls(id, parent, name, False, message, None)

class Result:
    """Result of a request to a device"""
    def __init__(self, ok: bool, message: str, systems: List[System]):
        self.time = str(datetime.now())
        self.ok = ok
        self.message = message
        self.systems = []
        if systems != None:
            self.systems = systems.copy()

    @classmethod
    def fromError(cls, message: str):
        return cls(False, message, None)

    @classmethod
    def fromSuccess(cls, systems: List[System]):
        return cls(True, None, systems)
