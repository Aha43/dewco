try:
	from sense_hat import SenseHat
except:
	try:
		from sense_emu import SenseHat
	except ImportError:
		from .sense_dummy import SenseHat

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
		available = sense != None
		state.append(Value.readOnly("available", available))
		if available:
			state.append(Value.readOnly("humidity", sense.get_humidity()))
		retVal.append(System.fromSuccess(self.name, state))
		return retVal
