import platform
from typing import Dict

from ..domain.model import System, Value


class SystemHandler:
    def __init__(self, name: str):
        self.name = name

    def state(self) -> System:
        pass

    def action(self, state: System) -> str:
        return "do not support actions"

SystemHandlers = Dict[str, SystemHandler]

def add_system_handler(handlers: SystemHandlers, h: SystemHandler) -> None:
    handlers[h.name] = h

def add_common_system_handlers(handlers: SystemHandlers) -> None:
    add_system_handler(handlers, PlatformSystemHandler())

class PlatformSystemHandler(SystemHandler):
    def __init__(self):
        super().__init__("platform")

    def state(self) -> System:
        data = platform.uname()
        state = []
        if (data[0]):
            state.append(Value.read_only("system", data[0]))
        if (data[1]):
            state.append(Value.read_only("node", data[1]))
        if (data[2]):
            state.append(Value.read_only("release", data[2]))
        if (data[3]):
            state.append(Value.read_only("version", data[3]))
        if (data[4]):
            state.append(Value.read_only("machine", data[4]))
        if (data[5]):
            state.append(Value.read_only("processor", data[5]))
        return System.from_success(self.name, state)
