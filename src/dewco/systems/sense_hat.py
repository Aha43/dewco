import importlib
from typing import Dict

from ..domain import System, Value
from ..util import get_env_var
from .handlers import SystemHandler, add_system_handler, SystemHandlers


def add_sense_hat_handlers(handlers: SystemHandlers) -> None:
    senseHat = None
    try:
        senseHatModule = get_env_var("__sense_hat_module__", "sense_hat")
        sense_module = importlib.import_module(senseHatModule)
        senseHat = sense_module.SenseHat()
    except:
        senseHat = None
    add_system_handler(handlers, SenseHatEnvironmentSystemHandler(senseHat))

class SenseHatEnvironmentSystemHandler(SystemHandler):
    def __init__(self, senseHat):
        super().__init__("sense_hat.environment")
        self.senseHat = senseHat

    def state(self) -> System:
        state = []
        state.append(Value.read_only("system-name", "SenseHat"))
        available = self.senseHat != None
        state.append(Value.read_only("available", available))
        if available:
            state.append(Value.read_only("humidity", self.senseHat.get_humidity()))
        return System.from_success(self.name, state)
