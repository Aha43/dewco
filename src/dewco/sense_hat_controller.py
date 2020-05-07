from sense_emu import SenseHat
from .controllers import SystemController
from typing import List
from .domain import System, Value

class SenseHatSystemController(SystemController):
		def __init__(self):
				super().__init__("SenseHat")

		def status(self) -> List[System]:
				retVal = []
				state = []
				sense = SenseHat()
				state.append(Value.readOnly("system-name", "SenseHat"))
				if sense != None:
						state.append(Value.readOnly("available", "false"))
				else:
						state.append(Value.readOnly("humidity", sense.get_humidity()))
                                retVal.append(System.fromSuccess(self.name, state))
                                return reversed
