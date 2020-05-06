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
		state = append(Value.readOnly("system-name", "SenseHat"))
		retVal.append(System.fromSuccess(self.name, state))
		return retVal
