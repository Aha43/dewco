import json

from datetime import datetime
from typing import List

class Value:
    """Represents a named value of a System state"""
    def __init__(self, name: str, value: object, type: str = "str", unit: str = None):
        self.name = name
        self.value = value
        self.type = type
        self.unit = unit

class System:
    """Represent state or desired sub state of a device System"""
    def __init__(self, name: str, ok: bool, message: str, state: List[Value]):
        self.name = name
        self.ok = ok
        self.message = message
        self.state = []
        if state != None:
            for v in state:
                self.state.append(v)

    @classmethod
    def fromSuccess(cls, name: str, state: List[Value]):
        return cls(name, True, None, state)

    @classmethod
    def fromError(cls, name: str, message: str):
        return cls(name, False, message, None)

class Result:
    """Result of a request to a device"""
    def __init__(self, ok: bool, message: str, systems: List[System]):
        self.time = str(datetime.now())
        self.ok = ok
        self.message = message
        self.systems = []
        if systems != None:
            for system in systems:
                self.systems.append(system)

    @classmethod
    def fromError(cls, message: str):
        return cls(False, message, None)

    @classmethod
    def fromSuccess(cls, systems: List[System]):
        return cls(True, None, systems)
