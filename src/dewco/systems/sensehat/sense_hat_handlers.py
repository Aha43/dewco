import importlib
import time
from typing import Dict, List

from ...domain.model import System, Value
from ...domain.units import Units
from ...domain.util import str_to_int, str_to_int_list
from ...util import get_env_var
from ..handlers import SystemHandler, SystemHandlers, add_system_handler


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
            if system.action == 'show_letters':
                return self.perform_show_letter(system)
            return "uknown action: " + system.action
        return "system not available"

    def perform_show_letter(self, system: System) -> str:
        letters = system.get_state_value("letters")
        sleep_head = str_to_int(system.get_state_value("sleep_head", "0"))
        sleep = str_to_int(system.get_state_value("sleep", "1"))
        rotation = str_to_int(system.get_state_value("rotation", "0"))
        text_color = str_to_int_list(system.get_state_value("text_color", "255,255,255"))
        back_color = str_to_int_list(system.get_state_value("back_color", "0,0,0"))
        
        if rotation != 0:
            self.senseHat.set_rotation(rotation)

        if sleep_head > 0:
            time.sleep(sleep_head)
        for c in letters:
            cs = str(c)
            self.senseHat.show_letter(cs, text_color, back_color)
            if (sleep > 0):
                time.sleep(sleep)
