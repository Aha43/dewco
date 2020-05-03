import json

from datetime import datetime

class Value:
    def __init__(self, name: str, value: object, type: str = "str", unit: str = None):
        self.name = name
        self.value = value
        self.type = type
        self.unit = unit


class System:
    def __init__(self, name: str, ok: bool, message: str, state):
        self.name = name
        self.ok = ok
        self.message = message
        self.state = []
        if state != None:
            for v in state:
                self.state.append(v)

    @classmethod
    def fromSuccess(cls, name: str, state):
        return cls(name, True, None, state)

    @classmethod
    def fromError(cls, name: str, message: str):
        return cls(name, False, message, None)


class Result:
    def __init__(self, ok: bool = True, message: str = None, *argv):
        self.time = str(datetime.now())
        self.ok = ok
        self.message = message
        self.systems = []
        for arg in argv:
            self.systems.append(arg)
