import importlib
import time
from typing import Dict, List

from ...domain import System, Value
from ...domain_util import str_to_int
from ...util import get_env_var, Units
from ..handlers import SystemHandler, add_system_handler, SystemHandlers

def add_sense_hat_handlers(handlers: SystemHandlers) -> None:
    senseHat = None
    try:
        senseHatModule = get_env_var("__sense_hat_module__", "sense_hat")
        sense_module = importlib.import_module(senseHatModule)
        senseHat = sense_module.SenseHat()
    except:
        senseHat = None
    add_system_handler(handlers, SenseHatEnvironmentSystemHandler(senseHat))
    add_system_handler(handlers, SenseHatLedSystemHandler(senseHat))

class BaseSenseHatSystemHandler(SystemHandler):
    def __init__(self, senseHat, subname: str):
        super().__init__("sense_hat." + subname)
        self.senseHat = senseHat
        self.available = self.senseHat != None

    def _get_base_state(self) -> List[Value]:
        state = []
        state.append(Value.read_only("system-name", self.name))
        state.append(Value.read_only("available", self.available))
        return state

class SenseHatEnvironmentSystemHandler(BaseSenseHatSystemHandler):
    def __init__(self, senseHat):
        super().__init__(senseHat, "environment")

    def state(self) -> System:
        state = self._get_base_state()

        if self.available:
            state.append(Value.read_only("humidity", self.senseHat.get_humidity(), Units.percentage_of_relative_humidity))
            state.append(Value.read_only("pressure", self.senseHat.get_pressure(), Units.millibars))
            state.append(Value.read_only("temperature", self.senseHat.get_temperature(), Units.celsius))
            state.append(Value.read_only("temperature_from_humidity", self.senseHat.get_temperature_from_humidity(), Units.celsius))
            state.append(Value.read_only("temperature_from_pressure", self.senseHat.get_temperature_from_pressure(), Units.celsius))
        
        return System.from_success(self.name, state)

class SenseHatLedSystemHandler(BaseSenseHatSystemHandler):
    def __init__(self, senseHat):
        super().__init__(senseHat, "led")
        self.senseHat = senseHat

    def state(self) -> System:
        state = self._get_base_state()
        return System.from_success(self.name, state)

    def action(self, system: System) -> str:
        if self.available:
            if system.action == 'show_letter':
                return self.perform_show_letter(system)
            return "uknown action: " + system.action
        return "system not available"

    def perform_show_letter(self, system: System) -> str:
        letters = system.get_state_value("letters")
        sleep = str_to_int(system.get_state_value("sleep", "1"))
        rotation = str_to_int(system.get_state_value("rotation", "0"))
        
        if rotation != 0:
            self.senseHat.set_rotation(rotation)

        for c in letters:
            cs = str(c)
            self.senseHat.show_letter(cs)
            time.sleep(sleep)
