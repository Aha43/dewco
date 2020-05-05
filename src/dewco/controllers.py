import platform

from typing import List

from .domain import System, Value

class SystemController:
    """Base class for classes which objects controls a device's system"""
    def __init__(self, name: str):
        self.name = name

    def status(self) -> List[System]:
        """Gets status of system in term of a System object"""
        pass

class PlatformSystemController(SystemController):
    def __init__(self):
        super().__init__("Platform")

    def status(self) -> List[System]:
        retVal = []
        data = platform.uname()
        state = []
        if (data[0]):
            state.append(Value.readOnly("system", data[0]))
        if (data[1]):
            state.append(Value.readOnly("node", data[1]))
        if (data[2]):
            state.append(Value.readOnly("release", data[2]))
        if (data[3]):
            state.append(Value.readOnly("version", data[3]))
        if (data[4]):
            state.append(Value.readOnly("machine", data[4]))
        if (data[5]):
            state.append(Value.readOnly("processor", data[5]))
        retVal.append(System.fromSuccess(self.name, state))
        return retVal
